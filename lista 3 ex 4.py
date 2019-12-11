A = []
B = []
for i in range(0, 5):
    A.append(int(input('Digite um valor para lista A:\n')))
for c in range(0, 5):
    B.append(int(input('Digite um valor para lista B:\n')))
for c in B:
    if(c % 2 == 0):
        A.append(c)

print('A lista A com numeros pares da lista B', A)
