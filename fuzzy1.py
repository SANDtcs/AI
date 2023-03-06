import matplotlib.pyplot as plt


speed= {"NL":[0,0,31,63],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255,255]}
acc= {"NL":[0,0,31,63],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255,255]}
throttle= {"NL":[0,0,31,63],"NM":[31,61,95],"NS":[61,95,127],"ZE":[95,127,159],"PS":[127,159,191],"PM":[159,191,223],"PL":[191,223,255,255]}

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
print(fuzzy_speed)


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
print(fuzzy_acc)

throttle={}

for i,j in zip(rules.keys(), rules.values()):
    if i[0] in fuzzy_speed and i[1] in fuzzy_acc:
        throttle[j]=min(fuzzy_speed[i[0]], fuzzy_acc[i[1]])
print(throttle)
