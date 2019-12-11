def media (L):
    soma = 0
    for item in L:
        soma = soma + item
    media = soma / len(L)
    return media
L = [2,5,10]
D = [2]
R = [1,5,8,7]
mR = media(R)
mD = media(D)
mL = media(L)
print('{:.2f}'.format(mL))
print(mR)
print(media(D))