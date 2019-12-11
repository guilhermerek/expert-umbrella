def produtorio (lista):
    if len(lista) == 0:
        return 0
    r = 1
    for i in lista:
        r = r * i
    return r
A = [2,3,7]
B = [3,-2]
C = [5,2.7]
D = []

print((produtorio(A) * produtorio(B) + produtorio(C)) * produtorio(D))
