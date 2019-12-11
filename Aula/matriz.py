# 0,1   0 é a linha  1 é a coluna

'''C = [
    [3,5,3],
    [1,4,-10]
]
B = [
    [2,3,4],
    [1,0,-3]
]'''

'''l = len(C)
f = len(C[0])
for i in range(0,l):
    for j in range(0,f):
        C[i][j] = 2*C[i][j]
print(C)'''



'''l = len(C)
f = len(C[0])
for i in range(0,l):
    for j in range(0,f):
        C[i][j] = B[i][j]+C[i][j]
print(C)'''
'''T=[]
l = len(C)
f = len(C[0])
for i in range(0,l):
    linha = []
    for j in range(0,f):
        v = B[i][j] + C[i][j]
        linha.append(v)
    T.append(linha)
print(T)'''


A = [
    [1,2,3,10],
    [4,5,6,11],
    [7,8,9,12],
    [13,14,15,16]
]
#diagonal principal
for b in range(0,len(A)):
    print(A[b][b])
#transposta
