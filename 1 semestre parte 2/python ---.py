def montarMatriz():
    M = []
    for m in range(0,5):
        linha = []
        for i in range (0,5):
            numero = int(input('digite um numero'))
            linha.append(numero)
        M.append(linha)
    return(M)
M = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    ]
soma = 0
for i in range(0, len(M[3])):
    soma = soma + M[3][i]
print(soma)
def somaLinhaMatriz(M, L):
    soma = 0
    for numero in M[L]:
        soma = soma + numero
    return soma
def somaDiagonalPrincipal(M):
    soma = 0
    for i in range (0,len(M)):
        soma = soma + M [i][i]
    return soma
def exercicio1 ():
    Matriz = montarMatriz ()
    soma = somaLinhaMatriz(Matriz, 3)
    print('soma da 4 linha =', soma)
    soma = somaDiagonalPrincipal(Matriz)
    print('Soma da diagonal principal = ', soma)
def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma
def media(lista):
    return somatorio(lista)/len(lista)

def exercicio2():
    n = int(input('digite um numero'))
    l = []
    while(n != -1):
        l.append(n)
        n = int(input('digite outro numero'))
    print(somatorio(l))
def exercicio3():
    nome = input('digite o nome do funcionario:')
    listanomes = []
    listasalarios = []
    salario = float(input('digite o salario:'))
    while(nome != 'fim'):
        listanomes.append(nome)
        listasalarios.append(salario)
        nome = input('digite o nome')
        if nome != 'fim':
            salario = float(input('digite o salario'))
    print('a media: ', media(listasalarios))
escolha = int(input('escolha o exercicio'))
if (escolha == 1):
    exercicio1()
elif escolha == 2:
    exercicio2()
elif escolha == 3:
    exercicio3()
