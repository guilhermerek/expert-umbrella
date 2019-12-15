def bemvindo(nome):
    print('Bem vindo,', nome)
    return nome
#bemvindo('Guilherme')

def maiorquecinco(n):
    if n > 5:
        print('Maior que cinco')
    elif n < 5:
        print('Menor que cinco')
    else:
        print('Igual à cinco')
#maiorquecinco(10)
#maiorquecinco(2)
#maiorquecinco(5)

def funcaomaior (n1,n2):
    if n1 > n2:
        return n1
    elif n1 == n2 or n2 == n1:
        return n1
    else:
        return n2
#print(funcaomaior(9,2))
#print(funcaomaior(1,98))
#print(funcaomaior(2,2))

def potencia (b,e):
    p = 1
    for i in range (0, e):
        p = p * b
    return p
#print(potencia(2,8))
#print(potencia(8,2))


def somatorio (l):
    resposta = 0
    for i in l:
        resposta = resposta + i
    return resposta
#print(somatorio([1,1,1,1]))
#print(somatorio([]))

def tabuada(n1):
    for i in range(0,11):
        print('{} * {} = {}' .format(n1, i, n1 * i))
#tabuada(4)

def escrever(lista, arquivo):
    arq = open (arquivo, 'w')
    arq.writelines(lista)
    arq.close()

a = input('Digite seu nome: \n')
respostas = []
respostas.append('Nome:' + a + '\n')
bemvindo(a)

escolha = 1
while escolha < 6:
    escolha = int(input('Digite o número da função:\n'))
    if escolha == 1:
        nume = int(input(('digite um número:\n')))
        maiorquecinco(nume)
    elif escolha == 2:
        n1 = int(input('Digite o primeiro número:\n'))
        n2 = int(input('Digite o segundo número:\n'))
        respostas.append('o maior e ' + str(funcaomaior(n1,n2)) + '\n')
        print(funcaomaior(n1,n2))
    elif escolha == 3:
        b = int(input('Digite a base: \n'))
        e = int(input('Digite o expoente: '))
        respostas.append(str(b)+' elevado a '+str(e) + ' = '+str(potencia(b,e))+'\n')
        print(potencia(b,e))
    elif escolha == 4:
        lista = []
        i = int(input('digite um numero: \n'))
        numerostr = str(i)
        while i != 0:
            lista.append(i)
            i = int(input('digite um numero:\n'))
            numerostr = numerostr + ','+ str(i)
        respostas.append('Soma de' + numerostr + '=' + str(somatorio(lista)) + '\n')
        print(somatorio(lista))
    elif escolha == 5:
        a = int(input('digite um numero para realizar a tabuada:\n'))
        tabuada(a)
else:
    print('função invalida')

escrever(respostas, 'arquivo ex sala.txt')
