lista = []
algo = str
retira = str
while(algo != 'fim'):
    algo = input('Digite o que irá adicionar:\n')
    if(algo in lista):
        print('Já está na sua lista!')
    else:
        lista.append(algo)

while(retira != 'fim'):
    retira = input('Digite o que ira remover:\n')
    if(retira in lista):
        lista.remove(retira)
    else:
        print('Não contem na lista!')
print('Restou na sua lista:', lista)
