altura = float(input('informe a altura'))
sexo = input('informe o sexo M ou F')
menor = altura
maior = altura
soma_altura_meninos = 0
qtd_meninos = 0
pos_alto = 0
sexo_alto = sexo
if(sexo == 'M'):
    soma_altura_meninos = soma_altura_meninos + altura
    qtd_meninos = qtd_meninos + 1
i = 1
while(i < 3):
    altura = float(input('informe a altura'))
    sexo = input('informe o sexo M ou F')
    if(altura < menor):
        menor = altura
    if(sexo == 'M'):
        soma_altura_meninos = soma_altura_meninos + altura
        qtd_meninos = qtd_meninos + 1
    if(altura > maior):
        maior = altura
        pos_alto = i + 1
        sexo_alto = sexo

    i = i + 1

print('Menor altura: ', menor)
if(qtd_meninos !=0):
    print('Media altura meninos: ', soma_altura_meninos / qtd_meninos)
else:
    print('Não existem nenhum menino na turma')
print('A pessoa mais alta é', sexo_alto, 'e esta na posição ', pos_alto)
