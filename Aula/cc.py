numero = int(input('digite um numero'))
primo = True

for i in range(2, numero):
    if(numero%i == 0):
        primo = False

if(primo == True):
    print(numero, 'é primo')
else:
    print(numero, 'nao é primo')
