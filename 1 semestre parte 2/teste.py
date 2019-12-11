'''arquivo = open('arqtest.txt', 'w')
texto = []
texto.append("lista alunos\n")
texto.append("fulano de tal \n")
texto.append("ciclano da silva \n")
#print(texto)
arquivo.writelines(texto)
arquivo.close()

#para ler o arquivo
arquivo = open('arqtest.txt', 'r')
texto = arquivo.readlines()
for linha in texto:
    print(linha)
arquivo.close()'''
#para nao sobscrever o que ja tinha
def ler():
    arquivo = open("arqtest.txt", "r")
    ler = arquivo.readlines()
    arquivo.close()
    return ler
A = ler()
for a in A:
    print(a)

def escrever(lista):
    arquivo = open("arqtest.txt", 'w')
    arquivo.writelines(lista)
    arquivo.close()
l = ["item 1\n", "item 2\n", "item3 \n"]
escrever(l)

B = ler()
B.append("item4\n")
escrever(B)