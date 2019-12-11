semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
dia_atual = input('Digite o dia atual:\n')
dia_de_volta = int(input('Quantos dias de férias irá tirar?\n'))
conta = 0
for c in range(0, len(semana)):
    if(dia_atual == semana[c]):
        conta = c
r = ((dia_de_volta+conta+1)%7)
volta = semana[r]
print(volta)
