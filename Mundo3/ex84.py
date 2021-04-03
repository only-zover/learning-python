temp = list()
princ = list()
b = l = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    
    if len(princ) == 0:
        b = l = temp[1]
    else:
        if temp[1] > b:
            b = temp[1]
        if temp[1] < l:
            l = temp[1]
    
    princ.append(temp[:])
    temp.clear()
            
    end = ' '
    while end not in 'SN':
        end = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    if end == 'N':
        break
    
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O menor peso é {l} kg. Peso de ',end = '')
for w in princ:
    if w[1] == l:
        print(w[0], end = ' ')
        
print(f'\nO maior peso é {b} kg. Peso de ', end = '')
for w in princ:
    if w[1] == b:
        print(w[0], end = ' ')
        