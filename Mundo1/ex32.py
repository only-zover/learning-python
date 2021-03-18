y = int(input('Digite um ano: '))

if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    print('{} é bissexto!'.format(y))
else:
    print('{} não é bissexto!'.format(y))
