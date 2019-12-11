print('-----------------')
print('Média aritmética')
print('----------------- \n')
i = 0
media = 0
while(i < 10):
    a = float(input('Digite um número: '))
    media = (media + a)
    i = i + 1
resultado = media / 10
print('O resultado da média aritmética é: {}' .format(resultado))
