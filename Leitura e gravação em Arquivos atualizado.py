def ler ():
    L = []
    arq = open("ead.txt", "r")
    a = arq.readlines()
    for item in a:
        N = int(item)
        L.append(N)
    arq.close()
    return L
def produtorio (N):
    prod = 1
    for i in N:
        prod = prod * i
    return prod
def somatorio (N):
    soma = 0
    for i in N:
        soma = soma + i
    return soma
def maior (N):
    m = max(N)
    for i in N:
        if i > m:
            m = i
    return m
def menor (N):
    me = min(N)
    for i in N:
        if i < me:
            me = i
    return me
def gravar (N):
    arq1 = open('arquivo.txt', 'w')
    arq1.writelines(N)
    arq1.close()
print('-'*30)
L = ler()
'''b = print('Multiplicação', produtorio(L))
c = print('Soma', somatorio(L))
d = print('Maior', maior(L))
e = print('Menor', menor(L))
f = print('-'*30)'''
texto = []
texto.append('-------------------------------\n')
texto.append('Multiplicação: {}\n' .format(produtorio(L)))
texto.append('Soma: {}\n' .format(somatorio(L)))
texto.append('Maior: {}\n' .format(maior(L)))
texto.append('Menor: {} \n' .format(menor(L)))
texto.append('-'*30)
gravar(texto)
def lerresultado ():
    arq = open('arquivo.txt', 'r')
    a = arq.readlines()
    arq.close()
    return a
print(lerresultado())