# A* algorithm
import numpy as np
import collections
import copy
state3=[[7,2,4],[5,0,6],[8,3,1]]
state2=[[1,2,3],[0,4,6],[7,5,8]]
state1=[[0,1,2],[3,4,5],[6,7,8]]

state=[[1,2,3],[4,5,6],[7,8,0]]

def heuristic_value(state):
    value=0
    num=1
    
    for i in range(0,3):
        for j in range(0,3):
            if state[i][j]!=num :
                value+=1
            num=(num+1)%9
    return value
def display(state):
    for i in state:
        print(i)
    print()


def convert_to_state(string):
    j=0;
    s=[]
    state=[]
    for j in range(0,3):
        for i in range(0,3):
            s.append(int(string[i+j*3]))
        state.append(s)
        s=[]
    return state

def convert_to_string(state):
    s=""
    for i in state:
        for j in i:
            s+=str(j)
    return s

def eight_puzzle_prob(state):
    
    val=heuristic_value(state);
    g=1
    visited=[]
    display(state)
    queue={}
    while(val>0):
        for i in range(0,3):
            if 0 in state[i]:
                r=i            
        c=state[r].index(0)   
        
        visited.append(convert_to_string(state))        
        row=[0,0,1,-1]
        col=[-1,1,0,0]
        state2=[]
        for i in range(0,4):
            r1=r+row[i]
            c1=c+col[i]
            if(r1>=0 and r1<3 and c1>=0 and c1<3):
                state2=copy.deepcopy(state)
                state2[r][c]=state2[r1][c1]
                state2[r1][c1]=0
                s=convert_to_string(state2)
                if(s not in visited):
                    #queue.append(state2)
                    queue[s]=heuristic_value(state2)+g
                    visited.append(s)
        queue=collections.OrderedDict(sorted(queue.items()))
        state=convert_to_state(list(queue.keys())[0])
        del queue[list(queue.keys())[0]]
        print(heuristic_value(state))
        g+=1
        display(state)
        val=heuristic_value(state)
        
eight_puzzle_prob(state)
