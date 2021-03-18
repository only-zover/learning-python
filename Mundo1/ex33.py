a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

smaller = a
if b < a and b < c:
    smaller = b
if c < a and c < b:
    smaller = c

bigger = a
if b > a and b > c:
    bigger = b
if c > a and c > b:
    bigger = c

print('O maior valor é {:.0f}\nO menor valor é {:.0f}'.format(bigger, smaller))