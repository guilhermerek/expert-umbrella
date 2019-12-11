print('-----------------------------------------')
print(' Quantos são pares e quantos são ímpares')
print('-----------------------------------------')
i = 0
cont1 = 0
cont2 = 0
while(i < 10):
    num = int(input('Digite um número: \n'))
    if(num % 2 == 0):
        print('O número {} é par' .format(num))
        cont1 = cont1 + 1
    else:
        print('O número {} é ímpar' .format(num))
        cont2 = cont2 + 1
    i = i + 1
print('Existe(m) {} número(s) pare(s) e {} ímpare(s)'.format(cont1, cont2))
