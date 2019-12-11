print('--------------------------------------------------------------------------------------')
print(' Determine se o aluno está reprovado, aprovado ou com exame com repetição de 30 notas')
print('--------------------------------------------------------------------------------------')
i = 0
soma = 0
while(i < 30):
    nota = float(input('Digite as notas:\n'))
    soma = soma + nota
    i = i + 1
media = soma / 30
if(media >= 7):
    print('Sua nota foi {:.2f}! E você foi aprovado!'.format(media))
elif(media < 4):
    print('Sua nota foi {:.2f}! E você foi reprovado!'.format(media))
else:
    print('Sua nota foi {:.2f}! E você está de exame!'.format(media))
