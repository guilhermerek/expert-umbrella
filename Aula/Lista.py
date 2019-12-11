#lista = [1,4,7,23,8]

'''for c in range(0, len(lista)):
    print(lista[c])'''
#print(len(lista) len é usado para contar


'''lista2 = [1,'b',3,['d','e',2,3]]
for c in lista2:
    print(c)'''

'''compras =['cafe', 'abacate', 'tomate']
comprei = ['coca', 'cafe', 'energetico']
for item in compras:
    if(not(item in comprei)):
        print('esqueci', item)

    else:
        print('Comprei', item)

for item in comprei:
    if(not(item in compras)):
        print('não precisava, mas comprei', item)'''


'''compras =['cafe', 'abacate', 'tomate']
comprei = ['coca', 'cafe', 'energetico']
for i in range (0, len(compras)):
    if(not(compras[i] in comprei)):
        print('esqueci', compras[i])
'''

compras =['cafe', 'abacate', 'tomate']
comprei = ['coca', 'cafe', 'energetico']
compras.append('uva')
print(compras)
compras.append('rapadura')
print(compras)
compras.insert(0, 'omo')
print(compras)
item = compras.pop(4)
print('Removi',item)
print(compras)
#compras.remove('omo')
compras.sort()
print(compras)
compras.reverse()
print(compras)

