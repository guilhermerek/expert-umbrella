print('----------------------------------------------')
print(' Ler 10 números e mostrar o produtório destes')
print('----------------------------------------------')
i = 0
prod = 1
while(i < 10):
    a = float(input('Digite algum número:\n'))
    prod = (prod * a)
    i = i + 1
print('O produtório dos números é:', (prod))
