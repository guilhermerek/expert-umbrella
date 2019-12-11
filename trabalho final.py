#Trabalho Guilherme Rek Castanha
#GRR: 20195403
resposta = []
def porcentagem (VT):
    if VT > 50000:
        comissao = VT * 0.12
    elif VT >= 30000 and VT <= 50000:
        comissao = VT * 0.095
    else:
        comissao = VT * 0.07
    return comissao
def media (m):
    total = 0
    for i in m:
        total += i
    media = total / len(m)
    return media
def linha4 (m):
    soma = 0
    for i in m[3]:
        soma = soma + i
    return soma
def somaDiagonalPrincipal(M):
    soma = 0
    for i in range (0,len(M)):
        soma = soma + M [i][i]
    return soma
def somamatriztoda(M):
    soma = 0
    for i in M:
        for j in i:
            soma += j
    return soma
def coluna(m):
        soma = 0
        for i in m:
            soma += i[1]
        return soma
def pg(ini, r, t):
    pg = []
    num = ini
    pg.append(num)
    for i in range(0, t):
        num *= r
        pg.append(num)
    return pg
def gravar(a):
    arq = open('respostafinal.txt', 'w')
    arq.writelines(a)
    arq.close()
y = str
while y != 'fim':
    y = input('Digite qual exercicio deseja executar:\n')
    if y == '1':
        c1 = input('Digite o nome do corretor:\n')
        venda1 = float(input('Digite o valor de vendas do primeiro corretor:\n'))
        c2 = input('Digite o nome do corretor:\n')
        venda2 = float(input('Digite o valor de vendas do segundo corretor:\n'))
        c3 = input('Digite o nome do corretor:\n')
        venda3 = float(input('Digite o valor de vendas do terceiro corretor:\n'))
        print('O corretor: {} recebeu a comissão de R$ {}' .format(c1, int(porcentagem(venda1))))
        print('O corretor: {} recebeu a comissão de R$ {}' .format(c2, int(porcentagem(venda2))))
        print('O corretor: {} recebeu a comissão de R$ {}' .format(c3, int(porcentagem(venda3))))
        print('A empresa lucrou em R$ {}' .format(int(venda3 + venda2 + venda1)))
        g = ('O corretor: {} recebeu a comissão de R$ {}' .format(c1, int(porcentagem(venda1))) + '\n')
        h = ('O corretor: {} recebeu a comissão de R$ {}' .format(c2, int(porcentagem(venda2))) + '\n')
        e = ('O corretor: {} recebeu a comissão de R$ {}' .format(c3, int(porcentagem(venda3))) + '\n')
        r = ('A empresa lucrou em R$ {}' .format(int(venda3 + venda2 + venda1)) + '\n')
        resposta.append(g)
        resposta.append(h)
        resposta.append(e)
        resposta.append(r)
    elif y == '2':
        nome = input('Digite o nome do cliente:\n')
        x = int(input('Digite a quantia de dias que o cliente irá ficar:\n'))
        diaria = 60
        if x > 15:
            taxa = 5.5
            valor = taxa * x + (x * diaria)
        elif x == 15:
            taxa = 6
            valor = taxa * x + (x * diaria)
        else:
            taxa = 8
            valor = taxa * x + (x * diaria)
        print('O cliente {} irá pagar R$ {} por {} dias' .format(nome, int(valor), x))
        f = ('O cliente {} irá pagar R$ {} por {} dias' .format(nome, int(valor), x) + '\n')
        resposta.append(f)
    elif y == '3':
        x = str
        total = 0
        msalario = []
        while x != 'fim':
            x = input('Digite o nome:\n')
            if x != 'fim':
                renda = float(input('Digite o salário:\n'))
                msalario.append(renda)
            elif len(msalario) == 0:
                print('Não há funcionários!')
                resposta.append('Não há funcionários!')

            else:
                print('A média salarial é: R$', media(msalario))
                print('O Menor salário é: R$', min(msalario))
                print('O maior salário é: R$', max(msalario))
                r = ('A média salarial é: R$', media(msalario))
                p = ('O Menor salário é: R$', min(msalario))
                w = ('O maior salário é: R$', max(msalario))
                resposta.append(r)
                resposta.append(p)
                resposta.append(w)
    elif y == '4':
        m = []
        for i in range(0, 5):
            linha = []
            for u in range(0, 5):
                n = int(input('Digite um número:\n'))
                linha.append(n)
            m.append(linha)
        print('Soma da linha 4:', linha4(m))
        print('Soma da Diagonal Principal:', somaDiagonalPrincipal(m))
        print('Soma total da matriz', somamatriztoda(m))
        print('Soma da Coluna 2', coluna(m))
        a = ('Soma da linha 4:', linha4(m))
        b = ('Soma da Diagonal Principal:', somaDiagonalPrincipal(m))
        c = ('Soma total da matriz', somamatriztoda(m))
        d = ('Soma da Coluna 2', coluna(m))
        resposta.append(a)
        resposta.append(b)
        resposta.append(c)
        resposta.append(d)
    elif y == '5':
        print(pg(2,2,8))
        a = (pg(2,2,8))
        resposta.append(a)
    elif y ==  '6':
        #valor dividido por 100 depois por % depois o q sobra de $ por 10 depois por % o que sobra de % por 1
        vtotal = int(input('Digite o valor da compra R$:\n'))
        v = int(input('Digite o valor que você recebeu R$:'))
        troco = v - vtotal
        a = troco / 100
        trococem = int(a)
        trocorestodecem = troco % 100
        trococemresto = trocorestodecem
        trocodez = trococemresto / 10
        trocorestodez = trococemresto % 10
        trocodezint = int(trocodez)
        trocoum = trocorestodez / 1
        print('O valor total é de R$ {}, seu troco foi de R$ {} e receberá {} notas de R$ 100, {} notas de R$ 10 e {} de R$ 1' .format(vtotal, troco, trococem, trocodezint, trocoum))
        n = ('O valor total é de R$ {}, o troco deve ser R$ {} e receberá {} notas de R$ 100, {} notas de R$ 10 e {} de R$ 1' .format(vtotal, troco, trococem, trocodezint, trocoum))
        resposta.append(n)
    elif y == '7':
        lista = []
        for i in range (0,20):
            a = int(input('Digite um número para adicionar à lista:\n'))
            lista.append(a)
        tamanho = len(lista)
        for i in range (0, int (tamanho/2)):
            aux = lista[i]
            lista[i] = lista[tamanho - 1 - i]
            lista[tamanho - 1 - i] = aux
        print(lista)
        resposta.append(lista)
    elif y == '8':
        num = int(input('Digite um número:\n'))
        semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
        if num > 7 or num < 0:
            print('ERROR 404')
            resposta.append('ERROR 404')
        else:
            print(semana[num])
            resposta.append(semana[num])
    else:
        print('Fim do programa!')
        gravar(str(resposta))