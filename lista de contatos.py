nome = []
telefone = []

for c in range(0,10):
    nome.append(input('Digite o nome:\n'))
    telefone.append(int(input('Digite o número do contato:\n')))

for c in range(0, len(nome)):
    print('Nome:', nome[c],'- Telefone:', telefone[c])
