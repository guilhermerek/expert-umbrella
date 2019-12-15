print('-'*15)
print('Exercício 2')
print('-'*15)
#a(n) = a(1) + (n-1) * r
primeiro = int(input('Digite o número inicial da P.A.:\n'))
razao = int(input('Escreva a razão desejada para P.A.:\n'))
i = 0
while(i < 10):
    print(primeiro)
    primeiro = primeiro + razao
    i = i + 1
