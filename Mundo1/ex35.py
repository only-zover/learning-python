l1 = float(input('Lado 1 do triângulo: '))
l2 = float(input('Lado 2 do triângulo: '))
l3 = float(input('Lado 3 do triângulo: '))

print('='*60)
if (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    print('É possivel formar um triângulo com os lados: {}, {} e {}.'.format(l1, l2, l3))
else:
    print('Não é possivel formar um triângulo com os lados: {}, {} e {}.'.format(l1, l2, l3))
print('='*60)
