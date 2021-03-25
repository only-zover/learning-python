print('10 PRIMEIROS TERMOS DE UMA P.A.')

a1 = int(input('1º termo: '))
r = int(input('Razão: '))
a = a1
c = 1
total = 0
more = 10

while more != 0:
    total += more
    while total >= c:
        c += 1
        a += r 
        print(a, end = ', ')
    print('PAUSA.\n')

    more = int(input('Número de termos que deseja ver: '))
print('\nFIM\n{} termos.'.format(total))
