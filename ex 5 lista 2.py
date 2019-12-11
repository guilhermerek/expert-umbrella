print('-'*15)
print('Excercício 5')
print('-'*15)
primeira = int(input('Digite a primeira tabuada a aparecer:\n'))
ultima = int(input('Digite a última tabuada à aparecer:\n'))
for a in range(primeira, ultima +1):
    for b in range(0, 11):
        print('{} * {} =' .format(a, b), a*b)
