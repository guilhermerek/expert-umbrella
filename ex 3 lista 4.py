n = int(input('Digite o número para fatorial:\n'))
lfat = []

for i in range(0, n):
    n = n - 1
    c = n + 1
    f = 1
    while c > 0:
        f = f * c
        c = c - 1

    lfat.append(f)
print(lfat)

