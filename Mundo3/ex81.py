values = list()
text = 'foi'

while True:
    n = int(input('Digite um valor: '))
    values.append(n)
    
    end = ' '
    while end not in 'SN':
        end = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if end == 'N':
        values.sort(reverse = True)
        break
    
if 5 not in values:
    text = 'não foi'
    
print(f'\nVocê digitou {len(values)} valores.\nOs valores em ordem descrecente são: {values}\nO valor 5 {text} encontrado!\n')
