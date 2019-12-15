A = [1,2,5,3]
C = [0,2,4,5,6,7]
D = []
for a in A:
    D.append(a)
    for c in C:
        if(c == a):
            D.remove(c)
print(D)
