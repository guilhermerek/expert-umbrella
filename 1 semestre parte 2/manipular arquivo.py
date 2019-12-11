#abre um arquivo para escrita (ja deve estr criado)
arq1 = open ('arquivo.txt', 'w')
# w escreve e r le
arq2 = open ('arquivo.txt', 'r')
arq1.write('Um texto\n')
arq1.writelines([])
a = arq2.readlines()
arq1.close()
arq2.close()