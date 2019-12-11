A = [1,2,3,4]
B = [2,4,6,1]
C = []
D = []
for a in A:
    for b in B:
        C.append([a,b])
'''for c in C:
    print(c)
'''
#fazer uniao de A com B e colocar na lista D
for a in A:
    D.append(a)
for b in B:
    if(not(b in D)):
        D.append(b)
for d in D:
    print(d)
