print('-'*15)
print('Exercício 3')
print('-'*15)
primeiro = int(input('Digite o primeiro termo da P.G.\n'))
razao = int(input('Digite a razão da P.G.\n'))
i = 0
while(i < 10):
    print(primeiro)
    primeiro = primeiro * razao
    i = i + 1
