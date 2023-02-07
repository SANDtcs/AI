import copy

def getFrogAdj(state):
    states = []
    temp = copy.deepcopy(state)
    for i in range(7):
      if temp[i] == 0 and i-1 >= 0 and temp[i-1] == 1:
        temp[i-1] = 0
        temp[i] = 1
        states.append(temp)
      temp = copy.deepcopy(state)
      if temp[i] == 0 and i+1 < len(temp) and temp [i+1] == 2:
        temp[i] = 2
        temp[i+1] = 0
        states.append(temp)
      temp = copy.deepcopy(state)
      if temp[i] == 0 and i-2 >= 0 and temp[i-2] == 1:
        temp[i] = 1
        temp[i-2] =0
        states.append(temp)
      temp = copy.deepcopy(state)
      if temp[i] == 0 and i+2 < len(temp) and temp[i+2] == 2:
        temp[i] = 2
        temp[i+2] = 0
        states.append(temp)
    return states


def frog(start, end):
    queue = [start,]
    
    while(len(queue)>0):
      curr = queue.pop(0)
      print(curr)
      if curr == end:
        return True
    
      adjStates = getFrogAdj(curr)
    
      for i in adjStates:
        queue.append(i)
    
    return False


initial = [1,1,1,0,2,2,2]
target = [2,2,2,0,1,1,1]

print(frog(initial,target))
