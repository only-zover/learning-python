n = int(input('Valor do saque: R$'))

fifty = n // 50
n %= 50

twenty = n // 20
n %= 20

ten = n // 10
n %= 10

one = n // 1

if fifty != 0:
    print(f'Total de {fifty:.0f} cédulas de R$50.00')
    
if twenty != 0:
    print(f'Total de {twenty:.0f} cédulas de R$20.00')
    
if ten != 0:
    print(f'Total de {ten:.0f} cédulas de R$10.00')

if one != 0:
    print(f'Total de {one:.0f} cédulas de R$1.00')
    