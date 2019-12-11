'''a = 9
for i in range(0,11):
    r = a*i
    print(a, '*', i, '=', r)'''

'''l = []
inicial = int(input('Digite o numero inicial da p.a.\n'))
razao = int(input('Digite a razao\n'))
a1 = inicial
print(a1)
for i in range(1,10):
    a1 = a1 + razao
    print(a1)'''
'''i = 0
c = 0
while (i < 10):
    a = int(input('digite um numero\n'))
    if (a % 2 == 0):
        r = a
        c = c + 1
    i = i + 1
print(c)'''
'''A = [8, 1, 4, 5]
B = [0, 2, 4, 5, 6, 7]
D = []
for a in A:
    if (a in B):
        D.append(a)
print(D)'''
'''A = [8, 1, 4, 5]
B = [0, 2, 4, 5, 6, 7]
D = []
for a in A:
    D.append(a)
for b in B:
    if (not(b in D)):
        D.append(b)
print(D)'''
'''A = [8, 1, 4, 5]
B = [0, 2, 4, 5, 6, 7]
D = []
for a in A:
    if (not(a in B)):
        D.append(a)
print(D)'''
'''n = 1
r = 0
while n != 0:
    n = float(input('Digite um número'))
    r = r + n

print(r)'''
'''from random import randint
tu = []
for i in range (0,100):
    numba = randint(0, 100)
    tu.append(numba)
tu.sort()
print(tu)'''

