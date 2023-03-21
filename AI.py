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




# **********************************************************************************
def forward_algorithm(sequence, states, emissions, transitions, initial_distribution):
    
    # Initialize the forward probabilities with zeros
    forward_probs = [{} for _ in range(len(sequence))]
    
    # Initialize the first forward probabilities using the initial distribution
    for state in states:
        forward_probs[0][state] = initial_distribution[state] * emissions[state][sequence[0]]
    
    # Recursively calculate the remaining forward probabilities
    for t in range(1, len(sequence)):
        for state in states:
            forward_probs[t][state] = emissions[state][sequence[t]] * sum(
                forward_probs[t-1][prev_state] * transitions[prev_state][state] for prev_state in states
            )
    
    # Calculate the total probability of the sequence as the sum of the final forward probabilities
    total_prob = sum(forward_probs[-1][state] for state in states)
    
    return forward_probs, total_prob


# Define the states, emissions, transitions, and initial distribution
states = ['h', 'l']
emissions = {
    'h': {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2},
    'l': {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3},
}
transitions = {
    'h': {'h': 0.5, 'l': 0.5},
    'l': {'h': 0.4, 'l': 0.6},
}
initial_distribution = {'h': 0.5, 'l': 0.5}

# Generate the gene sequence GGCA
sequence = 'GGCA'

# Run the forward algorithm
forward_probs, total_prob = forward_algorithm(sequence, states, emissions, transitions, initial_distribution)

# Print the results
print('Forward probabilities:')
for t in range(len(sequence)):
    print(f't = {t}:', forward_probs[t])
print('Total probability of the sequence:', total_prob)




# ****************************************** Viterbi ************************************************  
H = {'A': -2.322, 'C': -1.737, 'G': -1.737, 'T': -2.322}
L = {'A': -1.737, 'C': -2.322, 'G': -2.322, 'T': -1.737}
transitions = {('S', 'H'): -1, ('S', 'L'): -1, ('H', 'H'): -1, ('L', 'L'): -0.737, ('L', 'H'): -1.322, ('H', 'L'): -1}
seq = 'GGCACTGAA'
P = []
parent = []

for i in seq:
    if len(P) == 0:
        p = [transitions[('S', 'H')] + H[i], transitions[('S', 'L')] + L[i]]
    else:
        p = []
        par = []
        # H
        p.append(H[i] + max(P[-1][0] + transitions[('H', 'H')], P[-1][1] + transitions[('L', 'H')]))
        if P[-1][0] + transitions[('H', 'H')] > P[-1][1] + transitions[('L', 'H')]:
            par.append('H')
        else:
            par.append('L')
        # L
        p.append(L[i] + max(P[-1][0] + transitions[('H', 'L')], P[-1][1] + transitions[('L', 'L')]))
        if P[-1][0] + transitions[('H', 'L')] > P[-1][1] + transitions[('L', 'L')]:
            par.append('H')
        else:
            par.append('L')

        parent.append(par)
       
    P.append(p)
   
#print(P)
#print(parent)


path=[]

if P[-1][0] > P[-1][-1]:
    path.extend([par[0] for par in parent])
    path.append('H')
   
else:
    path.extend([par[1] for par in parent])
    path.append('L')
   
print(path)


# *************************************************** Viterbi3 ***********************************************************************
H = {'A': -2.322, 'C': -1.737, 'G': -1.737, 'T': -2.322}
L = {'A': -1.737, 'C': -2.322, 'G': -2.322, 'T': -1.737}
M = {'A': -1.737, 'C': -1.737, 'G': -2.322, 'T': -2.322}
transitions = {('S', 'H'): -1, ('S', 'L'): -1, ('S', 'M'): -1, ('H', 'H'): -1, ('L', 'L'): -0.737, ('M', 'M'): -1.322, ('H', 'L'): -1, ('L', 'H'): -1, ('H', 'M'): -1, ('L', 'M'): -1, ('M', 'H'): -1, ('M', 'L'): -1}
seq = 'GGCACTGAA'
P = []
parent = []


for i in seq:
    if len(P) == 0:
        p = [transitions[('S', 'H')] + H[i], transitions[('S', 'L')] + L[i],transitions[('S','M')]+M[i]]
    else:
        p = []
        par = []
        # H
        p.append(H[i] + max(P[-1][0] + transitions[('H', 'H')], P[-1][1] + transitions[('L', 'H')], P[-1][2] + transitions[('M', 'H')]))
        if P[-1][0] + transitions[('H', 'H')] > P[-1][1] + transitions[('L', 'H')] and P[-1][0] + transitions[('H', 'H')] > P[-1][2] + transitions[('M', 'H')]:
            par.append('H')
        elif P[-1][1] + transitions[('L', 'H')] > P[-1][2] + transitions[('M', 'H')]:
            par.append('L')
        else:
            par.append('M')
           
        # L
        p.append(L[i] + max(P[-1][0] + transitions[('H', 'L')], P[-1][1] + transitions[('L', 'L')], P[-1][2]+transitions[('M','L')]))
        if P[-1][0] + transitions[('H', 'L')] > P[-1][1] + transitions[('L', 'L')] and P[-1][0] + transitions[('H', 'L')] > P[-1][2] + transitions[('M', 'L')]:
            par.append('H')
        elif P[-1][1] + transitions[('L', 'L')] > P[-1][2] + transitions[('M', 'L')]:
            par.append('L')
        else:
            par.append('M')
           
        # M
        p.append(M[i] + max(P[-1][0] + transitions[('H', 'M')], P[-1][1] + transitions[('L', 'M')], P[-1][2]+transitions[('M','M')]))
        if P[-1][0] + transitions[('H', 'M')] > P[-1][1] + transitions[('L', 'M')] and P[-1][0] + transitions[('H', 'M')] > P[-1][2] + transitions[('M', 'M')]:
            par.append('H')
        elif P[-1][1] + transitions[('L', 'M')] > P[-1][2] + transitions[('M', 'M')]:
            par.append('L')
        else:
            par.append('M')
           
       

        parent.append(par)
       
    P.append(p)
   
#print(P)
#print(parent)


path=[]

if (P[-1][0] > P[-1][-1] and P[-1][1]>P[-1][2]):
    path.extend([par[0] for par in parent])
    path.append('H')
   
elif (P[-1][1]>P[-1][2]):
    path.extend([par[1] for par in parent])
    path.append('L')
else:
    path.append('M')
   
print(path)
