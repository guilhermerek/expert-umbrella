cardapio = []
i = str
a = str
while(i != 'finalizar'):
    i = input('O que deseja fazer: finalizar, inserir ou remover?\n')
    if(i == 'inserir'):
        a = input('O que deseja inserir no cardápio?\n')
        if(a in cardapio):
            print('Já está no cardápio!')
        else:
            cardapio.append(a)

    if(i == 'remover'):
        print('Você já incluiu no seu cardápio:', cardapio)
        a = input('O que deseja remover do cardápio?\n')
        if(a in cardapio):
            cardapio.remove(a)
        else:
            print('O que digitou não está no cardápio')
if(i == 'finalizar'):
    print('Foram pedidos:', len(cardapio), 'itens e as opções foram:', cardapio)
