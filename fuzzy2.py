import matplotlib.pyplot as plt


speed_diff={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],
            "PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
norm_acc={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],
          "PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
norm_throttle_control={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],
                       "ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}


rules={("NL","ZE"):"PL",("ZE","NL"):"PL",("NM","ZE"):"PM",("NS","PS"):"PS",
       ("PS","NS"):"NS",("PL","ZE"):"NL",("ZE","NS"):"PS",("ZE","NM"):"PM"}

def find_throttle_control(sd,acc):
    
    #CALCULATING THE SPEED DIFFERENCE MEMBERSHIP DEGREE
    sd_mem_deg={}
    for i in speed_diff:
        if(speed_diff[i][0]<=sd and speed_diff[i][2]>sd):
            a=speed_diff[i][0]
            b=speed_diff[i][1]
            c=speed_diff[i][2]
            deg=max(min((sd-a)/(b-a),(c-sd)/(c-b)),0)
            sd_mem_deg[i]=deg
    print("speed difference membership degree : ",sd_mem_deg,sep='\n')     
    
    #CALCULATING THE ACCELERATION MEMBERSHIP DEGREE
    acc_mem_deg={}
    for i in norm_acc:
        if(norm_acc[i][0]<=acc and norm_acc[i][2]>acc):
            a=norm_acc[i][0]
            b=norm_acc[i][1]
            c=norm_acc[i][2]
            deg=max(min((acc-a)/(b-a),(c-acc)/(c-b)),0)
            acc_mem_deg[i]=deg
    print("Acceleration membership degree : ",acc_mem_deg,sep='\n')   
    
    
    #FINDING THE THROTTLE MEMBER SIP DEGREE FOR CORRESPONDGIN FUZZY SET USING THE RULES
    throttle={}
    for i in rules:
        if(i[0] in sd_mem_deg and i[1] in acc_mem_deg):
            throttle[rules[i]]=min(sd_mem_deg[i[0]],acc_mem_deg[i[1]])
    print("Throttle membership degree : ",throttle,sep='\n')
    
    #CALCULAATING THE REGIONS
    polygon=[]
    regions=[]
    for i in throttle : 
        a=norm_throttle_control[i][0]
        b=norm_throttle_control[i][1]
        c=norm_throttle_control[i][2]
        polygon.append([[a,0],[b,1],[c,0],[a,0]])
        p=[[a,0]]
        x1=throttle[i]*(b-a) + a
        x2=(1-throttle[i])*(c-b) + b
        p.append([x1,throttle[i]])
        p.append([x2,throttle[i]])
        p.append([c,0])
        p.append(p[0])
        regions.append(p)
    print(polygon)
    
    
    
    #DEFUZZIFICATION : 
    total_area=0
    weighted_avg=0
    for p in regions:
        a=p[3][0]-p[0][0]
        b=p[2][0]-p[1][0]
        h=p[1][1]
        area=(a+b)*h/2
        centroid=(p[3][0]+p[0][0])/2
        print("centroid : ",centroid)
        weighted_avg+=area*centroid
        total_area+=area
    weighted_avg=weighted_avg/total_area

    #OUTPUT
    
    
    print("Throttle : ",weighted_avg)
    
    
    for j in norm_throttle_control:
        i=norm_throttle_control[j]
        t=[[i[0],0],[i[1],1],[i[2],0]]
        polygon.append(t)
    for i in polygon:
        xs,ys,=zip(*i)
        plt.plot(xs,ys)
    for i in regions:
        xs,ys,=zip(*i)
        plt.plot(xs,ys)
    plt.show()

sd=100
acc=70
find_throttle_control(sd, acc)
