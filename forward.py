H={'A':0.2,'C':0.3,'G':0.3,'T':0.2}
L={'A':0.3,'C':0.2,'G':0.2,'T':0.3}

transitions={('S','H'):0.5, ('S','L'):0.5, ('H','H'):0.5,
              ('L','L'):0.6,('L','H'):0.4,('H','L'):0.5}


seq='GGCA'
P=[]

for i in seq:
   
    if len(P)==0:
        p=[transitions[('S','H')]*H[i], transitions[('S','L')]*L[i]]
    else:
        p=[]
        p.append(P[-1][0] * transitions[('H','H')] * H[i] + P[-1][-1]*transitions[('L','H')]*H[i])
        p.append(P[-1][-1] * transitions[('L','L')] * L[i] + P[-1][0]*transitions[('H','L')]*L[i])
    P.append(p)
   
print(P)
print(P[-1][0] + P[-1][1])
