import matplotlib.pyplot as plt


speed={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
acceleration={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}
throttle_control={"NL":[0,31,61],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255]}


rules={("NL","ZE"):"PL",("ZE","NL"):"PL",("NM","ZE"):"PM",("NS","PS"):"PS",
       ("PS","NS"):"NS",("PL","ZE"):"NL",("ZE","NS"):"PS",("ZE","NM"):"PM"}

def find_throttle_control(sd,acc):
    
    #CALCULATING THE SPEED DIFFERENCE MEMBERSHIP DEGREE
    sd_mem_deg={}
    for i in speed:
        if(speed[i][0]<=sd and speed[i][2]>sd):
            a=speed[i][0]
            b=speed[i][1]
            c=speed[i][2]
            deg=max(min((sd-a)/(b-a),(c-sd)/(c-b)),0)
            #max(min((sd-a)/(b-a),1,(d-sd)/(d-c)),0)
            sd_mem_deg[i]=deg
    print("speed difference membership degree : ",sd_mem_deg,sep='\n')     
    
    #CALCULATING THE ACCELERATION MEMBERSHIP DEGREE
    acc_mem_deg={}
    for i in acceleration:
        if(acceleration[i][0]<=acc and acceleration[i][2]>acc):
            a=acceleration[i][0]
            b=acceleration[i][1]
            c=acceleration[i][2]
            deg=max(min((acc-a)/(b-a),(c-acc)/(c-b)),0)
            acc_mem_deg[i]=deg
    print("Acceleration membership degree : ",acc_mem_deg,sep='\n') 

    return acc_mem_deg,sd_mem_deg  
    


def fuzzification(sd_mem_deg,acc_mem_deg):
    #FINDING THE THROTTLE MEMBER SIP DEGREE FOR CORRESPONDGIN FUZZY SET USING THE RULES
    throttle={}
    for i in rules:
        if(i[0] in sd_mem_deg and i[1] in acc_mem_deg):
            throttle[rules[i]]=min(sd_mem_deg[i[0]],acc_mem_deg[i[1]])
    print("Throttle membership degree : ",throttle,sep='\n')

    return throttle
    

def calc_region(throttle):
    #CALCULAATING THE REGIONS
    polygon=[]
    regions=[]
    for i in throttle : 
        a=throttle_control[i][0]
        b=throttle_control[i][1]
        c=throttle_control[i][2]
        polygon.append([[a,0],[b,1],[c,0],[a,0]])
        p=[[a,0]]
        x1=throttle[i]*(b-a) + a
        x2=(1-throttle[i])*(c-b) + b
        p.append([x1,throttle[i]])
        p.append([x2,throttle[i]])
        p.append([c,0])
        p.append(p[0])
        regions.append(p)
    return polygon,regions
    
    
def defuzzification(polygon,regions):  
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
    for j in throttle_control:
        i=throttle_control[j]
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
acc_mem_deg,sd_mem_deg = find_throttle_control(sd, acc)
throttle=fuzzification(sd_mem_deg,acc_mem_deg)
polygon,regions=calc_region(throttle)
defuzzification(polygon,regions)
