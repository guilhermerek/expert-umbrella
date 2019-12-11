lista = ['banana', 'alface', 'cebola']

#print(lista[1])

'''
for i in range(0, len(lista)):
	print(lista[i])
'''


'''
for i in lista:
	print(i)
'''

'''
lista2 = ['palavra', ['a','b', 'c']]

print(lista2[1][0])
'''

'''
listaMercado = ['cebola', 'tomate', 'café', 'banana']
if('macarrão' in listaMercado):
	print("existe cebola")
else:
	print("não existe macarrão")
'''

'''
procurando = ['macarrão', 'cebola', 'alface', 'rabanete', 'tomate', ]

encontrou = ['macarrão', 'cebolinha', 'tomate', 'café']
achei = 0
for produto in procurando:
	if(produto in encontrou):
		print("Encontrei ", produto)
		achei = achei+1
	else:
		print("Não encontrei ", produto)
print("encontrei ",( 1-((len(procurando)-achei)/len(procurando)) )," dos produtos que procurava" )
'''

'''
print('lista\n')
for produto in lista:
	print(produto)

print('\nadicionando abacate\n')
lista.append('abacate')
for produto in lista:
	print(produto)


print('\nadicionando ameixa no inicio\n')
lista.insert(0, 'ameixa')
for produto in lista:
	print(produto)

print('\nretirando segundo item \n')
banana = lista.pop(1)
for produto in lista:
	print(produto)


print("produto retirado: ", banana)

print('\nretirando item abacate \n')
banana = lista.remove("abacate")
for produto in lista:
	print(produto)


#programa inserir itens

print('CARRINHO DE COMPRAS')

lista = []

produto = input('digite cada produto da sua lista de compras, e tecle enter \n quando finalizar digite fim\n\n')
while(produto != 'fim'):
	lista.append(produto)
	produto = input('digite ...\n ')

lista.sort()
print("-"*5,"Lista de compras","-"*5)
for p in lista:
	print(p)
print(len(lista),"itens na lista")
print("-"*30)



encontrado = []
produto = input('digite cada item que você comprou\n quando finalizar, digite fim\n\n')
while(produto != 'fim'):
	encontrado.append(produto)
	produto = input('digite ...\n ')

encontrado.sort()
print("-"*5,"produtos comprados","-"*5)
for p in encontrado:
	print(p)
print(len(encontrado),"itens na lista")
print("-"*30)

for p in lista:
	if(p in encontrado):
		print("comprei ",p)
	else:
		print("não encontrei ", p)

for e in encontrado:
	if(e not in lista):
		print("comprei ",e,"mesmo não estando na lista")





lista2 = []

produto = input('digite cada produto e depois a qtdade da sua lista de compras, e tecle enter \n quando finalizar digite fim\n\n')
qtd = int(input('quantidade\n'))

while(produto != 'fim'):
	lista2.append([produto, qtd])
	produto = input('produto\n ')
	if(produto != 'fim'):
		qtd = int(input('quantidade\n'))
print("-"*30)

for p, q in lista2:
	print(p,": ",q)


print("-"*30)

for item in lista2:
	print(item[0],": ",item[1])
'''

'''
semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado" , "domingo"]
s_atual = input('dia da semana')

ferias = int(input('dias de férias'))



for i in range(0, len(semana)):
	if(s_atual == semana[i]):
		indice_semana_atual = i

dias = ((ferias+indice_semana_atual+1)%7);


s_voltar = semana[dias]
print(s_voltar)
'''


'''
nomes = []
telefones = []
for i in range(1, 5):
	nome = input('digite o nome')
	telefone = input('digite o telefone')
	nomes.append(nome)
	telefones.append(telefone)

for i in range(0, len(nomes)):
	print(nomes[i]," : ",telefones[i])
'''

'''
telefones = []
for i in range(1, 5):
	nome = input('digite o nome')
	telefone = input('digite o telefone')
	telefones.append([nome,telefone])

for n, t in telefones:
	print(n," : ",t)
'''

'''
pedido = []
digitado = ""
while(digitado != "finalizar"):
	digitado = input("escolha: inserir, finalizar ou remover\n")
	if(digitado == "inserir"):
		produto = input("digite o produto que quer\n")
		pedido.append(produto)	
	elif(digitado == "remover"):
		print("-"*10)
		for p in pedido:
			print(p)
		print("-"*10)
		produto = input("digite o produto que quer remover\n")
		pedido.remove(produto)	
	

print("-"*10)
for p in pedido:
	print(p)
print("-"*10)
print(len(pedido)," itens")

'''









