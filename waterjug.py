import copy

def getAdjStates(curr):
    
    states = []
    temp = copy.deepcopy(curr)
    
    
    # Filling 3 gallon jug
    if temp[0] + 3 <= 3:
      temp[0] += 3
      states.append(temp)
    temp = copy.deepcopy(curr)
      
    
    # Filling 4 gallon jug
    if temp[1] + 4 <= 4:
      temp[1] += 4
      states.append(temp)
    temp = copy.deepcopy(curr)
      
      
    # Pouring into 4 gallon jug
    if temp[0] != 0:
      n = temp[0] + temp[1]
      diff = 4 - n
      if diff <= 0:
        temp[0] = abs(diff)
        temp[1] = 4
      else:
        temp[0] = 0
        temp[1] = n
      states.append(temp)
    temp = copy.deepcopy(curr)
      
    
    # Pouring into 3 gallon jug
    if temp[1] != 0:
      n = temp[0] + temp[1]
      diff = 3 - n
      if diff <= 0:
        temp[1] = abs(diff)
        temp[0] = 3
      else:
        temp[1] = 0
        temp[0] = n
      states.append(temp)
    temp = copy.deepcopy(curr)
      
    
    # Emptying 3 gallon jug
    if temp[0] != 0:
      temp[0] = 0
      states.append(temp)
    temp = copy.deepcopy(curr)
    
    
    # Emptying 4 gallon jug
    if temp[1] != 0:
      temp[1] = 0
      states.append(temp)
      
      
    return states


path = []
visited = []

def dfs(node, end):
  if node == end:
    visited.append(node)
    return True
  visited.append(node)
  adjstates = getAdjStates(node)
  print(node)
  print(adjstates)
  for i in adjstates:
    if i not in visited:
      #print(i)
      if dfs(i, end):
        path.append(i)
        return True
      else:
        return False

dfs([0,0], [0, 2])
print(path)
