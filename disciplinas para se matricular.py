listad = ['matematica', 'portugues', 'historia', 'geografia', 'ciencias']
lista007 = []
print('As disciplinas são: matematica, portugues, historia, geografia, ciencias')
opcao = str

while(opcao != 'finalizar'):
    opcao = input('Informe o que ira fazer: finalizar, escolher, retirar:\n')
    if (opcao == 'escolher'):
        print(listad)
        dis = input('Digite a disciplina que irá cursar:\n')
        lista007.append(dis)
        listad.remove(dis)
    elif (opcao == 'retirar'):
        print(lista007)
        dis = input('Digite a disciplina que escolher para cursar:\n')
        lista007.remove(dis)
        listad.append(dis)
    elif (opcao == 'finalizar'):
        if (len(lista007) < 3) or (len(lista007) == 0):
            print('A quantidade de materias escolhidas é insuficiente escolha mais matérias:')
            opcao = input('Informe o que ira fazer: finalizar, escolher, retirar:\n')
            if (opcao == 'escolher'):
                print(listad)
                dis = input('Digite a disciplina que irá cursar:\n')
                lista007.append(dis)
        elif (len(lista007) > 3):
            u = len(lista007) - 3
            print('Você escolheu mais que 3 matérias, remova:{}'.format(u))
            opcao = input('Informe o que ira fazer: finalizar, escolher, retirar:\n')
        elif(len(lista007) == 3):
            print(lista007)
