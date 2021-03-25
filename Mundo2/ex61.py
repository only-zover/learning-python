print('10 PRIMEIROS TERMOS DE UMA P.A.')

a1 = int(input('1º termo: '))
r = int(input('Razão: '))
a = a1
c = 1

while 10 >= c:
    c += 1
    a += r 
    print(a, end = ', ')
print('\nFIM\n')