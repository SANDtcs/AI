left=[3,3,1]

def check_valid(state,cnt):
    m1=state[0]
    c1=state[1]
    m2=cnt-m1
    c2=cnt-c1
    if(m1<0 or m1>cnt or c1<0 or c1>cnt):
        return False    
    if((m1>0 and c1>m1) or (m2>0 and c2>m2)):
        return False
        
    return True
    
def alter(s,t,j):
    res=[s[i]+j*t[i] for i in range(3)]
    return res 



def MandC(cnt):
    
    state=[cnt,cnt,1]
    moves=[[2,0,1],[1,0,1],[0,1,1],[0,2,1],[1,1,1]]
    
    stack=[]
    state2=[]
    visited=[]
    stack.append(state)
    visited.append(state)
    while(len(stack)>0):
        print(state)
        side=state[2]
        if(state==[0,0,0]):
            print("End state reached")
            return
        for i in moves:
            if side==1:
                state2=alter(state,i,-1 )
                if(check_valid(state2,cnt) and state2 not in visited):
                    stack.append(state2)
                    visited.append(state2)
            else :
                state2=alter(state,i,1)
                if(check_valid(state2,cnt) and state2 not in visited):
                    stack.append(state2)
                    visited.append(state2)
    
        state=stack[len(stack)-1]
        del stack[-1]
         
    print("Ended")
    
    
    
MandC(2)
