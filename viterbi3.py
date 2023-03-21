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
