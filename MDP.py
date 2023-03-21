from copy import deepcopy

sun={"wind":1/2,"sun":1/2}
wind={"hail":1/2,"sun":1/2}
hail={"hail":1/2,"wind":1/2}

sun_reward=4
wind_reward=0
hail_reward=-8


expected={"sun":sun_reward,"wind":wind_reward,"hail":hail_reward}
for i in range(300):
    prev=deepcopy(expected)
    expected["sun"]=sun_reward+0.9*sum(sun[x]*prev[x] for x in sun.keys())
    expected["wind"]=wind_reward+0.9*sum(wind[x]*prev[x] for x in wind.keys())
    expected["hail"]=hail_reward+0.9*sum(hail[x]*prev[x] for x in hail.keys())
   
print(expected)


# ***************************************************************************
from copy import deepcopy


PU={'S':{'PU':1},'A':{'PU':1/2,'PF':1/2}}
PF={'S':{'PU':1/2,'RF':1/2},'A':{'PF':1}}
RF={'S':{'RF':1/2,'RU':1/2}, 'A':{'PF':1}}
RU={'S':{'PU':1/2,'RU':1/2}, 'A':{'PU':1/2,'PF':1/2}}

actions=['S','A']

PU_reward=0
PF_reward=0
RF_reward=10
RU_reward=10

def find_max(action, state, values, prev):
    sum_vals=[]
    for i in action:
        sum_vals.append(sum(values[i][x] * prev[x] for x in values[i].keys()))
    return max(sum_vals)

expected = {"PU":PU_reward, "PF":PF_reward, "RF":RF_reward, 'RU':RU_reward}


for i in range(300):
    prev=deepcopy(expected)
   
    expected["PU"] = PU_reward + 0.9 * find_max(actions, "PU", PU, prev)
    expected["PF"] = PF_reward + 0.9 * find_max(actions, "PF", PF, prev)
    expected["RF"] = RF_reward + 0.9 * find_max(actions, "RF", RF, prev)
    expected["RU"] = RU_reward + 0.9 * find_max(actions, "RU", RU, prev)
   
print(expected)
