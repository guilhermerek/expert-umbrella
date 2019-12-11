'''numero = int(input('digite um numero'))
primo = True

for i in range(2, numero):
	if(numero%i == 0):
		primo = False

if(primo == True):
	print(numero,"é primo")
else:
	print(numero, "não é primo")'''


primo = True
primos = []
for i in range(1, 101):
    for j in range(2, i):
        if(i%j == 0):
            primo = False
        if(primo == True):
            primos.append(i)
print(primos)
