def positivoOunegativo (n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
#crie um laço de repetição de -10 até 10 e usem
#a função acima para verificar quem é positivo, negativo ou neutro
#for i in range (-10, 11):
#    positivoOunegativo(i)
soma = 0
for i in range(0,5):
    n = int(input('Digite um numero \n'))
    if positivoOunegativo(n) == 1:
        soma = soma + n
print(soma)
