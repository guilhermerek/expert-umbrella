lista = []
for i in range(0, 100):
    from random import randint
    a = randint(0, 100)
    lista.append(a)
    lista.sort()
for i in lista:
    print(i)
