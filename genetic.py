import sympy as sp
import numpy as np
import random
x,y=sp.symbols('x,y')



def randombin(n):
    list1=[0,1]
    i="";
    for t in range(n):
        i=i+str(random.choice(list1))
    return i

def convertToDec(n):
    t=0
    for i in n:
        t=t*2+int(i)
    return t

def normalization(l,h,n,i):
    return l+(h-l)*i/pow(2,n)


n=10
f=(x**2+y-11)**2+(x+y**2-7)**2
limit=[0,6]

x1=[]
x2=[]
for i in range(5):
    x1.append(randombin(n))    
    x2.append(randombin(n))
    
print(x1,x2,sep='\n')
x1=["1110010000","0001001101","1010100001","1001000110","1100011000"]
x2=["1100100000","0011100111","0111001000","1000010100","1011100011"]
x1=[normalization(limit[0],limit[1],n,convertToDec(i)) for i in x1]
x2=[normalization(limit[0],limit[1],n,convertToDec(i)) for i in x2]
print(x1,x2,sep='\n')

fx=[f.replace(x,x1[i]).replace(y,x2[i]) for i in range(5)]
print(fx)
Fx=[1/(1+i) for i in fx]
print(Fx)
sumFx=0
for i in Fx:
    sumFx+=i
print(sumFx)

p=[i/sumFx for i in Fx]
print(p)
cumP=[]
t=0
for i in p:
    r=t+i
    cumP.append(r)
    t=r
print(cumP)
