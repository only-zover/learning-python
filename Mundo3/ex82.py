values = []
odd = []
even = []

while True:
    n = int(input('Digite um valor: '))
    values.append(n)
    
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n) 
    
    end = ' '
    while end not in 'SN':
        end = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if end == 'N':
        break
        
print(f'\nA lista completa: {values}.\nA lista de pares: {even}.\nA lista de ímpares: {odd}.\n')
