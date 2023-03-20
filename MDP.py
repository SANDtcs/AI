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
