num = int(input('Digite um número inteiro: '))
print(' ')
print('Escolha uma das bases para a conversão:\n[ 1 ] Converter para BINÁRIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL')
typed = int(input('Sua opção: '))

base = ''
final = ''

if typed == 1:
    base = 'BINÁRIO'
    final = bin(num)[2:]
elif typed == 2:
    base = 'OCTAL'
    final = oct(num)[2:]
elif typed == 3:
    base = 'HEXADECIMAL'
    final = hex(num)[2:]

print(' ')
print('{} convertido para {} é igual a {}.'.format(num, base, final))
