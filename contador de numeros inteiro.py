print('-'*25)
soma = 0
for c in range(1, 6):
    n = float(input('Digite algum número:\n'))
    if(n % 1 ==0):
        soma = soma + 1
    else:
        print('Esse número não é inteiro')
print('Existem {} números inteiros' .format(soma))
