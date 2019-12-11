A = []
B = []
for i in range(0, 10):
    A.append(int(input('Digite um valor:\n')))
for c in range(0, 10):
    B.append(int(input('Digite outro valor:\n')))
for i in A:
    for c in B:
        print('O número {} multiplicado por {} é: {}' .format(i, c, i*c))
