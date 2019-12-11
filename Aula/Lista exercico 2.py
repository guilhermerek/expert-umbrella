''''nomes = []
emails = []
for i in range(0, 5):
    nome = input('digite o nome\n')
    email = input('digite email\n')
    nomes.append(nome)
    emails.append(email)
for i in range(0 ,len(nomes)):
    print(nomes[i], ':', emails[i])
'''''

contatos = []
for i in range(0, 5):
    nome = input('digite o nome\n')
    email = input('digite email\n')
    contatos.append([nome, email])
for item in contatos:
    print(item[0], ':', item[1])


''''for a in contatos:
    print(a, ':', b)'''