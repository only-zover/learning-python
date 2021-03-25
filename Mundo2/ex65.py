c = n = s = big = low = 0
stay = ' '

while stay not in 'nN':
    n = int(input('Digite um número: '))
    c += 1
    s += n

    if c == 1:
        big = low = n
    else:
        if n > big:
            big = n
        if n < low:
            low = n
   
    stay = str(input('Quer continuar? [S/N] ')).strip() 
    
    while stay not in 'nNsS':
        stay = str(input('Por favor, apenas "S" ou "N"\nQuer continuar? [S/N] ')).strip() 
        
print('\nVocê digitou {} números.\nA média: {:.2f}.\nO maior valor: {}.\nO menor valor: {}.\n'.format(c, s / c, big, low))
