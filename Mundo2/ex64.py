s = c = 0

n = int(input('Digite um número [999 para sair]: '))

while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número [999 para sair]: '))
    
print('\nVocê digitou {} números.\nA soma entre eles é {}.\n'.format(c, s))
