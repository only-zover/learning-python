from random import randint
from time import sleep

print('| [ 1 ] PEDRA   |\n| [ 2 ] PAPEL   |\n| [ 3 ] TESOURA |')

you = int(input('Escolha: '))
cpu = int(randint(1,3))

if you < 1 or you > 3:
    exit('ERRO!\nEscolha 1, 2 ou 3.')

print('JO'), sleep(0.8), print('KEN'), sleep(0.9), print('PO'), sleep(0.5)

itens = ['','PEDRA', 'PAPEL', 'TESOURA']
final = 'Você ganhou.'
youText = 'Você escolheu {}'.format(itens[you])
cpuText = 'Computador escolheu {}'.format(itens[cpu])

if you == cpu:
    final = 'Empate.'
elif you == 1 and cpu == 2 or you == 2 and cpu == 3 or you == 3 and cpu == 1:
    final 
else:
    final = 'Você perdeu.'

print(' '), print(youText), sleep(1), print(cpuText), sleep(0.3), print(final)
