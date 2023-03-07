import matplotlib.pyplot as plt
import numpy as np


speed= {"NL":[0,31,63],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255,255]}
acc= {"NL":[0,31,63],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255,255]}
throttle= {"NL":[0,31,63],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255,255]}

x=np.array([0,31,61,95,127,159,191,223,255])
y1=np.array([1,1,0,1,0,1,0,1,1])
y2=np.array([0,0,1,0,1,0,1,0,0])


rules={("NL","ZE"):"PL",("ZE","NL"):"PL",("NM","ZE"):"PM",("NS","PS"):"PS",("PS","NS"):"NS",("PL","ZE"):"NL",("ZE","NS"):"PS",("ZE","NM"):"PM"}

speed_val=100
acc_val=70

fuzzy_speed={}
for i,j in zip(speed.keys(),speed.values()):
   
    if speed_val in range(j[0],j[2]):    
        if i=="NL":
            if speed_val<j[1]:
                fuzzy_speed[i]=1
            else:
                c=j[1]
                d=j[2]
                fuzzy_speed[i]=(d-speed_val)/(d-c)
               
        elif i=="PL":
            if speed_val>j[1]:
                fuzzy_speed[i]=1
            else:
                a=j[0]
                b=j[1]
                fuzzy_speed[i]=(speed_val-a)/(b-a)
        else:      
            a=j[0]
            b=j[1]
            c=j[2]
            fuzzy_speed[i]=round(max(min((speed_val-a)/(b-a), (c-speed_val)/(c-b)),0),4)
#print("Fuzzy Speed:",fuzzy_speed)


fuzzy_acc={}
for i,j in zip(acc.keys(),acc.values()):
    if acc_val in range(j[0],j[2]):
        if i=="NL":
            if acc_val<j[1]:
                fuzzy_acc[i]=1
            else:
                c=j[1]
                d=j[2]
                fuzzy_acc[i]=(d-acc_val)/(d-c)
               
        elif i=="PL":
            if acc_val>j[1]:
                fuzzy_acc[i]=1
            else:
                a=j[0]
                b=j[1]
                fuzzy_acc[i]=(acc_val-a)/(b-a)
        else:      
            a=j[0]
            b=j[1]
            c=j[2]
            fuzzy_acc[i]=round(max(min((acc_val-a)/(b-a), (c-acc_val)/(c-b)),0),4)
#print("Fuzzy Acceleration:",fuzzy_acc)

fuzzy_throttle={}

for i,j in zip(rules.keys(), rules.values()):
    if i[0] in fuzzy_speed and i[1] in fuzzy_acc:
        fuzzy_throttle[j]=min(fuzzy_speed[i[0]], fuzzy_acc[i[1]])
#print("Fuzzy Throttle:",fuzzy_throttle)


polygon=[]
regions=[]

for i in fuzzy_throttle:
    a=throttle[i][0]
    b=throttle[i][1]
    c=throttle[i][2]
   
    polygon.append([[a,0],[b,1],[c,0],[a,0]])
    p=[[a,0]]
    x1=fuzzy_throttle[i]*(b-a) + a
    x2=(1-fuzzy_throttle[i])*(c-b) + b
    p.append([x1,fuzzy_throttle[i]])
    p.append([x2,fuzzy_throttle[i]])
    p.append([c,0])
    p.append(p[0])
    regions.append(p)
print("Polygon:",polygon)
   
total_area=0
weighted_avg=0

for p in regions:
    a=p[3][0]-p[0][0]
    b=p[2][0]-p[1][0]
    h=p[1][1]
   
    area=(a+b)*h/2
    centroid=(p[3][0]+p[0][0])/2
    print("Area:",area)
    print("centroid : ",centroid)
    weighted_avg+=area*centroid
    total_area+=area
   

weighted_avg=weighted_avg/total_area

print("Throttle:",weighted_avg)

for j in throttle:
    i=throttle[j]
    if j=="NL":
        t=[[i[0],0],[i[0],1],[i[1],1],[i[2],0]]
        polygon.append(t)
    elif j=="PL":
        t=[[i[0],0],[i[1],1],[i[2],1],[i[2],0]]
        polygon.append(t)
    else:
        t=[[i[0],0],[i[1],1],[i[2],0]]
        polygon.append(t)
       
print("Polygon:",polygon)
print("Regions:",regions)
for i in polygon:
    xs,ys,=zip(*i)
    plt.plot(xs,ys)
for i in regions:
    xs,ys,=zip(*i)
    plt.plot(xs,ys)
plt.show()
