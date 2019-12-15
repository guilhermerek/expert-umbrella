
matriz1 = []
matriz2 = []
resultado = []

for coluna in range(0, 2):
    linha = []
    for l in range(0, 2):
        elem = int(input(f'Digite {coluna} {l}: '))
        linha.append(elem)
    matriz1.append(linha)

for coluna in range(0, 2):
    linha = []
    for l in range(0, 2):
        elem = int(input(f'Digite {coluna} {l}: '))
        linha.append(elem)
    matriz2.append(linha)

for i in range(0, len(matriz1)):
    linha = []
    for j in range(0, len(matriz1[0])):
        res = matriz1[i][j] + matriz2[i][j]
        linha.append(res)
    resultado.append(linha)

print(f'Matriz1 {matriz1} e \nMatriz2 {matriz2}')
print(f'Resultado {resultado}')
