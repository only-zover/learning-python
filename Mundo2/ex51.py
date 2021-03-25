print('10 PRIMEIROS TERMOS DE UMA P.A.')

a1 = int(input('1º termo: '))
r = int(input('Razão: '))

for x in range(a1, a1 + (10) * r, r):
    print(x, end = ', ')
print('FIM')
