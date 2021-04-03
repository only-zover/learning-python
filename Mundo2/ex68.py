from random import randint

result = resultText = c = 0
even = 'even'
odd = 'odd'
choice = ' '
final = 'IMPAR'

print('PAR ou ÍMPAR')

while True:
    
    pc = randint(1, 10)
    u = int(input('Escolha o valor: '))
    choice = str(input('PAR ou ÍMPAR? [P/I] ')).strip()
    
    while choice not in 'pPiI':
        choice = str(input('Por favor, apenas "P" ou "I"\nPAR ou ÍMPAR? [P/I] ')).strip()
    
    if choice in 'pP':
        choice = even
    if choice in 'iI':
        choice = odd
    
    result = u + pc
    resultText = u + pc

    if result % 2 == 0:
        result = even
        final = 'PAR'
    else:
        result = odd
        final = 'ÍMPAR'
        
    print(f'\nVocê jogou {u} e o computador {pc}.\nTotal {resultText}.\nDEU {final}.')
    
    if choice != result:
        break
    else: print('Você venceu!')

    c += 1

print(f'\nVocê perdeu!\nVocê venceu {c} vezes.\n')
