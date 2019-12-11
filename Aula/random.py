#from random import randint
print('-'*20)
print('Exercício 1 lista 2')
print('-'*20)
i = 0
maior = 0
menor = 101
while(i < 10):
    numero = randint(0, 100)
    print(numero)
    if(numero > maior):
        maior = numero
    elif(numero < menor):
        menor = numero
    i = i + 1

print('O maior número aleatório é: {} e o menor é: {}' .format(maior, menor))
