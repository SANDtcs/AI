import copy

PU = {"A":{"PU":0.5, "PF":0.5}, "S":{"PU":1}}
PF = {"A":{"PF":1}, "S":{"PU":0.5, "RF":0.5}}
RF = {"A":{"PF":1}, "S":{"RU":0.5, "RF":0.5}}
RU = {"A":{"PF":0.5, "PU":0.5}, "S":{"RU":0.5, "PU":0.5}}

rewards = {"PU":0, "PF":0, "RU":10, "RF":10}

expected = {"PU":rewards["PU"], "PF":rewards["PF"], "RU":rewards["RU"], "RF":rewards["RF"]}

for i in range(1000):
  prev = copy.deepcopy(expected)
  temp = {"PU":[], "PF":[], "RU":[], "RF":[]}
  for x in PU.keys():
    temp["PU"].append(sum(PU[x][y]*prev[y] for y in PU[x].keys()))
  expected["PU"] = rewards["PU"] + 0.9* max(temp["PU"])
  for x in PF.keys():
    temp["PF"].append(sum(PF[x][y]*prev[y] for y in PF[x].keys()))
  expected["PF"] = rewards["PF"]+0.9*max(temp["PF"])
  for x in RU.keys():
    temp["RU"].append(sum(RU[x][y]*prev[y] for y in RU[x].keys()))
  expected["RU"] = rewards["RU"]+0.9*max(temp["RU"])
  for x in RF.keys():
    temp["RF"].append(sum(RF[x][y]*prev[y] for y in RF[x].keys()))
  expected["RF"] = rewards["RF"]+0.9*max(temp["RF"])
  if max(abs(prev[state] - expected[state]) for state in expected.keys()) < 1e-5:
    print(i)
    break

print(expected)
