a = int(input('digite a'))
b = int(input('digite b'))
c = int(input('digite c'))

delta = ((b)**2)-4*a*c
raiz = delta**0.5
if(raiz > 0)or(raiz == 0):
    x1 = (-b + raiz)/(2*a)
    x2 = (-b - raiz)/(2*a)
    print(x1, x2)
else:
    print('não existe')
print(raiz, delta)
