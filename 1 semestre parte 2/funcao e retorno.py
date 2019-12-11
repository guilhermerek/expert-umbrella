'''n1 = int(input('digite um n'))
n2 = int(input('digite outro n'))
def meu_pow(n1,n2):
    result = 1

    for i in range(0,n2):
        result = n1*result
    print(result)
meu_pow(n1,n2)'''

'''def oi():
    print('hello world')

oi()'''

'''def bemvindo(nome):
    print('Hello,', nome)
def bemvindo2(nome = "sem nome"):
    print('Hello, ,', nome)
bemvindo2("Australopitecus")
bemvindo2()'''

'''#Real soma(numero1, numero2)
def soma(n1,n2):
    result = n1 + n2
    return result
n1 = float(input('digite'))
n2 = float(input('digite'))
print(soma(n1,n2))'''

#Real meu_pow(Real n1,Inteiro n2)
#retornar numero1 elevado ao numero2
'''def meu_pow(a,b):
    r = 1
    for i in range(0,b):
        r = a * r
    return r
print(meu_pow(2,5))'''

#real media_aritmetica(lista lista)
#Retornar a media aritmetica dos elementos de uma lista numerica
'''l = [2,3,4,5]
tamanho = len(l)
soma = 0
for i in l:
    soma = soma + i
if (tamanho == 0):
    media = 0
else:
    media = soma/tamanho
print(media)'''

'''def media_aritmetica(l):
    tamanho = len(l)
    soma = 0
    media = 0
    for i in l:
        soma = soma + i
    if (tamanho == 0):
        media = 0
    else:
        media = soma / tamanho
    return media
print(media_aritmetica([2,3,5,1,0.5,7]))
print(media_aritmetica([2]))
print(media_aritmetica([]))
print(media_aritmetica([0,10]))'''

#procedimento que, informando um numero inteiro, deve imprimir a tabuada desse numero
#desde 0 até 10

#tabuada(numero)

def tabuada(n1):
    for i in range(0,11):
        print(n1*i)
tabuada(7)
for i in range(1,11):
    print('tabuada', i)
    tabuada(i)