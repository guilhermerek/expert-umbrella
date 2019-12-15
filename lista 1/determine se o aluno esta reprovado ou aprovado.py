print('-------------------------------------------------')
print(' Determine se o aluno está reprovado ou aprovado ')
print('-------------------------------------------------')
n1 = float(input('Digite a primeira nota:\n'))
n2 = float(input('Digite a segunda nota:\n'))
n3 = float(input('Digite a terceira nota:\n'))
media = (n1 + n2 + n3)/3
if(media >= 7):
    print('Sua nota foi {}! E você foi aprovado!'.format(media))
elif(media < 4):
    print('Sua nota foi {}! E você foi reprovado!'.format(media))
else:
    print('Sua nota foi {}! E você está de exame!'.format(media))
if(media >= 4):
    n5 = float(input('Digite a nota que tirou no exame:\n'))
    exame = (media + n5)/2
    if(exame >= 5):
        print('Sua nota foi {}! E você está aprovado por exame!'.format(exame))
    elif(exame <= 5):
        print('Sua nota foi {}! E você está reprovado por exame!'.format(exame))
