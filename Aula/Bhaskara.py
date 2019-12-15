import math
a = int(input('digite a'))
b = int(input('digite b'))
c = int(input('digite c'))

delta = ((b)**2)-4*a*c

if(delta >= 0):
    raiz = delta ** 0.5
    x1 = (-b + raiz)/(2*a)
    x2 = (-b - raiz)/(2*a)
    print(x1, x2)
else:
    print('não existe')
print(delta)
