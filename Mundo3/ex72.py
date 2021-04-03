cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    while n < 0 or n > 20:
        n = int(input('Digite um número de 0 a 20: '))
    
    stop = str(input('Quer continuar? [S/N] ')).strip().upper()
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N] ')).strip().upper()
        
    if stop in 'N':
        break
    
print('\nFIM\n')