cheapName = ''
total = expensive = cheap = n = 0

while True:
    name = str(input('Nome do produto: ')).strip()
    price = float(input('Preço: R$'))
    
    n += 1
    
    if n == 1 or n < cheap:
        cheap = price
        cheapName = name 
    
    if price > 1000:
        expensive += 1
    
    total += price
    
    end = ' '
    while end not in 'sSnN':
        end = str(input('Quer continuar? [S/N] ')).strip()[0]
    
    if end in 'nN':
        break
    
print(f'\nTotal da compra: R${total:.2f}.\nTemos {expensive} produtos custando mais de R$1000.00.\nO produto mais barato é a {cheapName} que custa R${cheap:.2f}.\n')
