import copy

constraints = [[True,True,False,False],[True,True,True,False],[False,True,True,False],[False,False,True,True],[False,False,False,True],[True,False,False,True]]

def getNextStates(curr):
    states = []
    temp = copy.deepcopy(curr)
    
    if temp[3] == True:
      temp[3] = False
    else:
      temp[3] = True
    states.append(temp)
    temp = copy.deepcopy(curr)
    
    if temp[3] == True:
      temp[3] = False
    else:
      temp[3] = True
    
    for i in range(3):
      if temp[i] != temp[3]:
        temp[i] = not temp[i]
        states.append(temp)
        temp = copy.deepcopy(curr)
        if temp[3] == True:
          temp[3] = False
        else:
          temp[3] = True
    res = []
    for i in states:
      if i not in constraints:
        res.append(i)
    return res


def manTiger(start, end):
    queue = [start,]
    visited = []
    
    while(len(queue)!=0):
      curr = queue.pop(0)
      print(curr)
      if curr == end:
        return True
      visited.append(curr)
      
    
      adjStates = getNextStates(curr)
      for i in adjStates:
        if i not in visited and i not in queue:
          queue.append(i)
      
    return False

# Tiger,Goat,Grass,Boat
start=[True,True,True,True]
end=[False,False,False,False]

print(manTiger(start, end))
