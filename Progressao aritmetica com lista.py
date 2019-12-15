pro = int(input("Digite o número inicial:\n"))
r = int(input('Digite a razão:\n'))
lista = []
lista.append(pro)
for i in range(0, 10):
    pro = pro + r
    lista.append(pro)
print(lista)
