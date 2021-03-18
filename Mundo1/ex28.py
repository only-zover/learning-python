from random import randrange

userN = int(input('Escolha um número entre 1 a 5: '))

cpuN = randrange(6)

if userN == cpuN:
    print('O número correto é {}.\nO seu número é {}\nParabéns! Acertou!'.format(cpuN, userN))
else:
    print('O número correto é {}.\nO seu número é {}\nMais sorte na próxima!'.format(cpuN, userN))
