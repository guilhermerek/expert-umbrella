def mul(A, B):
    linha_A, coluna_A = len(A), len(A[0])
    linha_B, coluna_B = len(B), len(B[0])
    assert coluna_A == linha_B
    C = []
    for linha in range(linha_A):
        #adicionando uma linha nova na lista C com elementos da linha A
        C.append([])
        for coluna in range(coluna_B):
            #adicionando uma coluna nova na lista C com elementos da coluna B
            C[linha].append(0)
            for K in range(coluna_A):
                #agora realiza a mutiplicação de matrizes
                C[linha][coluna] = C[linha][coluna] + A[linha][K] * B[K][coluna]
    return C

A = [
    [1,2,3],
    [4,5,6]
]
B = [
    [5,9],
    [8,4],
    [3,2]
]
print(mul(A,B))