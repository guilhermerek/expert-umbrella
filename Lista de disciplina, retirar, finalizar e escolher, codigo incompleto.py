listad = ['matematica', 'portugues', 'historia', 'geografia', 'ciencias']
lista007 = []
print('As disciplinas são: matematica, portugues, historia, geografia, ciencias')
opcao = str
i = 1
while(opcao != 'finalizar'):
    opcao = input('Informe o que ira fazer: finalizar, escolher, retirar:\n')
    if (opcao == 'escolher'):
        print(listad)
        dis = input('Digite a disciplina que irá cursar:\n')
        lista007.append(dis)
        listad.remove(dis)


    elif (opcao == 'retirar'):
        print(lista007)
        dis = input('Digite a disciplina que irá cursar:\n')
        lista007.remove(dis)
        listad.append(dis)

    elif(opcao == 'finalizar'):
        print(lista007)

        if (len(lista007) < 3):
            opcao = input('Informe o que ira fazer: finalizar, escolher, retirar:\n')
            if (opcao == 'escolher'):
                print(listad)
                dis = input('Digite a disciplina que irá cursar:\n')
                lista007.append(dis)


        if (len(lista007) > 3):
            u = len(lista007) - 3
            print('Você escolheu mais que 3 matérias, remova:{}'.format(u))
            opcao = input('Informe o que ira fazer: finalizar, escolher, retirar:\n')
            if (opcao == 'retirar'):
                print(lista007)
                dis = input('Digite a disciplina que irá cursar:\n')
                lista007.remove(dis)
                listad.append(dis)
