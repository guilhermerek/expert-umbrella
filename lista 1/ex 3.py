print('------------')
print('Par ou ímpar')
print('------------')
soma = 0
i = 0
while(i < 10):
    num = int(input('Digite um número: \n'))
    if(num % 2 == 0):
        print('O número {} é par'.format(num))
    else:
        print('O número {} é ímpar' .format(num))
    i = i + 1
