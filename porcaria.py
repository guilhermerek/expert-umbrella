disciplinas = ['mat','port','geo','hist','ciencias','logica']
escolhidas = []
print('disciplinas disponiveis')
for d in disciplinas:
    print(d)
comando = input('Digite escolher, remover ou finalizar')
while(comando != 'finalizar'):
    if(comando == 'escolher'):
            if(len(escolhidas)<3):
                print(disciplinas)
                m = input('qual materia deseja adicionar')
                escolhidas.append(m)
                disciplinas.remove(m)
            else:
                print('vc ja escolheu 3')
                
    elif(comando == 'remover'):
        print(escolhidas)
        m = input('qual materia deseja remover')
        escolhidas.remove(m)
        disciplinas.append(m)

    if(comando == 'finalizar'):
        if(len(escolhidas)!= 3):
            print('Vc precisa escolher 3 materias')
            comando = 'escolher'
print(escolhidas)
