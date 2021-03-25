s = 0
cPair = 0

for x in range(1, 7):
    n = int(input('{}º inteiro: '.format(x)))
    if n % 2 == 0:
        s += n
        cPair += 1
print('{} valores pares\nA soma entre eles é {}.'.format(cPair, s))
