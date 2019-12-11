print('---------------------------------------')
print('Média aritmética dos números positivos!')
print('---------------------------------------')
i = 0
soma = 0
while(i < 10):
    a = float(input('Digite um número para realizar a média:\n'))
    if(a > 0):
        soma = soma + a
    i = i + 1
media = soma/10
print('Média dos positivos é {:.2f}'.format(media))
