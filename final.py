'''
Viterbi Algorithm

H = {'A': -2.322, 'C': -1.737, 'G': -1.737, 'T': -2.322}
L = {'A': -1.737, 'C': -2.322, 'G': -2.322, 'T': -1.737}
transitions = {('S', 'H'): -1, ('S', 'L'): -1, ('H', 'H'): -1, ('L', 'L'): -0.737, ('L', 'H'): -1.322, ('H', 'L'): -1}
seq = 'GGCACTGAA'
P = []
parent = []

for i in seq:
   
    if len(P)==0:
        p=[transitions[('S','H')]+H[i], transitions[('S','L')]+L[i]]
   
    else:
        p=[]
        par=[]
       
        p.append(H[i]+max(P[-1][0]+transitions[('H','H')], P[-1][1]+transitions[('L','H')]))
       
        if P[-1][0]+transitions[('H','H')] > P[-1][1]+transitions[('L','H')]:
            par.append('H')
        else:
            par.append('L')
           
        p.append(L[i]+max(P[-1][-1]+transitions[('L','L')], P[-1][0] + transitions[('H','L')]))
       
        if P[-1][-1]+transitions[('L','L')]> P[-1][0] + transitions[('H','L')]:
            par.append('L')
        else:
            par.append('H')
           
        parent.append(par)
       
    P.append(p)
   
#print(P)
#print(parent)


path=[]

if P[-1][0]>P[-1][-1]:
    path.extend([par[0] for par in parent])
    path.append('H')
else:
    path.extend([par[1] for par in parent])
    path.append('L')
   
print(path)'''



#Forward Algorithm

'''H={'A':0.2,'C':0.3,'G':0.3,'T':0.2}
L={'A':0.3,'C':0.2,'G':0.2,'T':0.3}

transitions={('S','H'):0.5, ('S','L'):0.5, ('H','H'):0.5,
              ('L','L'):0.6,('L','H'):0.4,('H','L'):0.5}


seq='GGCA'

P=[]

for i in seq:
   
    if len(P)==0:
        p=[transitions[('S','H')]*H[i] , transitions[('S','L')] * L[i]]
       
    else:
        p=[]
        p.append(P[-1][0]*transitions[('H','H')]*H[i] + P[-1][-1] * transitions[('L','H')] * H[i])
        p.append( L[i] * (P[-1][-1] * transitions[('L','L')] + P[-1][0] * transitions[('H','L')]))
    P.append(p)
   
print(P)

'''

#Markov Decision Process
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
