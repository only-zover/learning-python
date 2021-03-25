Max = int(input('Quantidade de termos: '))
c = 3
n1 = 0
n2 = 1

print('{} - {}'.format(n1, n2), end = ' - ')
while c <= Max:
    n3 = n1 + n2
    print('{}'.format(n3), end = ' - ')
    n1 = n2
    n2 = n3
    c += 1
    
print('fim')

