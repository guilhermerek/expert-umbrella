'''Crie as seguintes funções:

Função que receba uma lista de string, converta todos em inteiros e retorne o
 produtório de todos os itens

Função que receba uma lista de string, converta todos em inteiros e retorne o
 somatório de todos os itens

Função que receba uma lista de string, converta todos em inteiros e retorne o
 maior elemento.

Função que receba uma lista de string, converta todos em inteiros e retorne o
 menor elemento.'''
O = []
arq = open("ead.txt", "r")
a = arq.readlines()
O.append(a)
arq.close()
print(O)
for i in O:
    a = i
    a = int
    print(a)