import matplotlib.pyplot as plt


speed_diff={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],
            "PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
norm_acc={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],
          "PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
norm_throttle_control={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],
                       "ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}


rules={("NL","ZE"):"PL",("ZE","NL"):"PL",("NM","ZE"):"PM",("NS","PS"):"PS",
       ("PS","NS"):"NS",("PL","ZE"):"NL",("ZE","NS"):"PS",("ZE","NM"):"PM"}

sd = 120
a = 100



def findMemValue(reg,x):
    val = max(min((x-reg[0])/(reg[1]-reg[0]),(reg[2]-x)/(reg[2]-reg[1])),0)
    return val

def findAcc(a):
    acc_mem = {}
    for key in norm_acc:
        if((a <= norm_acc[key][2] and a >= norm_acc[key][1]) or (a <= norm_acc[key][1] and a>=norm_acc[key][0])):
            acc_mem[key] = findMemValue(norm_acc[key], a)
    return acc_mem

def findSd(a):
    sd_mem = {}
    for key in speed_diff:
        if((a <= speed_diff[key][2] and a >= speed_diff[key][1]) or (a <= speed_diff[key][1] and a>=speed_diff[key][0])):
            sd_mem[key] = findMemValue(norm_acc[key], a)
    return sd_mem

def findThrottle(a,sd):
    acc = findAcc(a)
    sdiff = findSd(sd)
    throttle = {}
   
    for key in rules:
        if key[0] in sdiff and key[1] in acc:
            throttle[rules[key]] = min(sdiff[key[0]],acc[key[1]])
    return throttle

def fuzzyfication(a,sd):
    return findThrottle(a, sd)

print(fuzzyfication(a,sd))   




from posixpath import join
def findArea(triangle,throttle):
  a = [triangle[0],0]
  b = [triangle[1],1]
  c = [triangle[2],0]

  # y-y1/y2-y1 = x-x1/x2-x1
  # x = ((y-y1)/(y2-y1))*(x2-x1) + x1
  # for p1 : x1 = a, x2 = b
  # for p2 : x1 = b, x2 = c

  p1x = ((throttle - a[1])/(b[1] - a[1]))*(b[0] - a[0]) + a[0]
  p2x = ((throttle - b[1])/(c[1] - b[1]))*(c[0] - b[0]) + b[0]

  return 0.5*throttle*((p2x-p1x)+(c[0]-a[0]))

def findCentroid(triangle,throttle):
  a = [triangle[0],0]
  b = [triangle[1],1]
  c = [triangle[2],0]

  # y-y1/y2-y1 = x-x1/x2-x1
  # x = ((y-y1)/(y2-y1))*(x2-x1) + x1
  # for p1 : x1 = a, x2 = b
  # for p2 : x1 = b, x2 = c

  p1x = ((throttle - a[1])/(b[1] - a[1]))*(b[0] - a[0]) + a[0]
  p2x = ((throttle - b[1])/(c[1] - b[1]))*(c[0] - b[0]) + b[0]

  return (a[0]+c[0])/2

def findIntersection(triangle,throttle):
  a = [triangle[0],0]
  b = [triangle[1],1]
  c = [triangle[2],0]

  # y-y1/y2-y1 = x-x1/x2-x1
  # x = ((y-y1)/(y2-y1))*(x2-x1) + x1
  # for p1 : x1 = a, x2 = b
  # for p2 : x1 = b, x2 = c

  p1x = ((throttle - a[1])/(b[1] - a[1]))*(b[0] - a[0]) + a[0]
  p2x = ((throttle - b[1])/(c[1] - b[1]))*(c[0] - b[0]) + b[0]

  return p1x,p2x

def defuzzyfication(throttleFuzzy):
  areas = {}
  centroids = {}
  for key in throttleFuzzy:
    areas[key] = findArea(norm_throttle_control[key],throttleFuzzy[key])
    centroids[key] = findCentroid(norm_throttle_control[key],throttleFuzzy[key])

  x=0
  y=0
  for i in throttleFuzzy: 
    x+=areas[i]*centroids[i]
    y+=areas[i]
  return x/y




def plot(throttleFuzzy):
  polygon = []
  regions = []
  throttleSet = []

  for i in norm_throttle_control:
    temp = []
    if i == "PL":
      temp.append([0,0])
      temp.append([norm_throttle_control[i][0],0])
      temp.append([norm_throttle_control[i][1],1])
      temp.append([255,1])
      temp.append([255,0])

    if i == "NL":
      temp.append([0,0])
      temp.append([0,1])
      temp.append([norm_throttle_control[i][1],1])
      temp.append([norm_throttle_control[i][2],0])

    else:
      temp.append([norm_throttle_control[i][0],0])
      temp.append([norm_throttle_control[i][1],1])
      temp.append([norm_throttle_control[i][2],0])

    throttleSet.append(temp)


  for i in throttleFuzzy:
      a = norm_throttle_control[i][0]
      b = norm_throttle_control[i][1]
      c = norm_throttle_control[i][2]
      polygon.append([[a, 0], [b, 1], [c, 0], [a, 0]])
      i1,i2 = findIntersection(norm_throttle_control[i],throttleFuzzy[i])
      regions.append([[a,0],[i1,throttleFuzzy[i]],[i2,throttleFuzzy[i]],[c,0],[a,0]])
  for i in throttleSet:
      p1, p2 = zip(*i)
      plt.plot(p1, p2)
  print(throttleSet)
  for i in regions:
      p1, p2 = zip(*i)
      plt.plot(p1, p2)




defuzzyfication(fuzzyfication(a,sd))



plot(fuzzyfication(a,sd))


