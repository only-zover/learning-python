v = list()

while True:
    n = int(input('Digite um valor: '))
    
    if n not in v:
        v.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não vou adicionar!')
    
    end = ' '
    while end not in 'SN':
        end = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if end == 'N':
        v.sort()
        break
    
print(f'\nVocê digitou os valores {v}.\n')
