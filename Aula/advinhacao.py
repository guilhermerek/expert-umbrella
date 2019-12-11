from random import randint
numero = randint (0, 10)
palpite = int(input('advinhe o numero'))
while(palpite != numero):
    if(palpite > numero):
        print('Muito alto')
    else:
        print('Muito baixo')
    palpite = int(input('digite de novo '))
print('Voce acertou ', numero)