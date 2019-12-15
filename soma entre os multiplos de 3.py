print('-'*25)
soma = 0
for c in range(1,6):
    n1 = float(input('Digite um número para realizar a soma:\n'))
    if(n1 % 3 == 0):
        soma = soma + n1
print('A soma entre os múltiplos de 3 é:', soma)
