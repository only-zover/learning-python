num = ( int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')) )

text3 = '\nO valor 3 apareceu na {num.index(3)+1}ª posição.'

if 3 not in num:
    text3 = 'Não há 3'
print(f'\nVocê digitou os valores: {num}.\nO valor 9 apareceu {num.count(9)} vezes.')
print('Os valores pares são: ', end = '')

for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
