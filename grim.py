def triangular_member(x,points):
  val = max(min((x-points[0])/(points[1]-points[0]),(points[2]-x)/(points[2]-points[1])),0)
  #plt.plot(points,[0,1,0])
  #plt.scatter(x,val)
  return val



def trapezoidal_member(x,points):
  val = max(min((x-points[0])/(points[1]-points[0]),1,(points[3]-x)/(points[3]-points[2])),0)
  #plt.plot(points,[0,1,0])
  #plt.scatter(x,val)
  return val



def fuzzy_controller(sd,a):
  speed_difference = {"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
  acceleration = {"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
  throttle_control = {"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
  rules = {("NL","ZE"):"PL",("ZE","NL"):"PL",("NM","ZE"):"PM",("NS","PS"):"PS",("PS","NS"):"NS",("PL","ZE"):"NL",("ZE","NS"):"PS",("ZE","NM"):"PM"} 

  speed_mem = {}
  acc_mem = {}
  throttle = {}

  for i in speed_difference:
    if(speed_difference[i][0] < sd and speed_difference[i][2] > sd):
      speed_mem[i] = triangular_member(sd,speed_difference[i])
  for i in acceleration:
    if(acceleration[i][0] < a and acceleration[i][2] > a):
      acc_mem[i] = triangular_member(a,acceleration[i])

  for i in rules:
    if(i[0] in speed_mem and i[1] in acc_mem):
      throttle[rules[i]] = min(speed_mem[i[0]],acc_mem[i[1]])
    
  polygon = []
  region =[]

  for i in throttle_control:
    a = throttle_control[i][0]
    b = throttle_control[i][1]
    c = throttle_control[i][2]
    if(i == "NL"):
      polygon.append([[0,1],[b,1],[c,0]])
    elif(i == "PL"):
      polygon.append([[a,0],[b,1],[c,1]])
    else:
      polygon.append([[a,0],[b,1],[c,0]])
    

  for i in throttle:
    a = throttle_control[i][0]
    b = throttle_control[i][1]
    c = throttle_control[i][2]
    #polygon.append([[a,0],[b,1],[c,0]])
    region.append([[a,0], [throttle[i]*(b-a)+a,throttle[i]], [(1-throttle[i])*(c-b)+b,throttle[i]], [c,0], [a,0]])


  print(speed_mem,acc_mem,throttle)
  weightedSum = 0
  totalArea = 0

  for i in polygon:
        p1, p2 = zip(*i)
        plt.plot(p1, p2)

  for i in region:
        p1, p2 = zip(*i)
        plt.plot(p1, p2)
        lower = i[3][0] - i[0][0]
        upper = i[1][0] - i[2][0]
        h = i[1][1]
        area = (upper + lower) * h / 2

        weightedSum += area * ((i[2][0] + i[1][0]) / 2)
        totalArea += area
  plt.show()
  print(weightedSum/totalArea)
