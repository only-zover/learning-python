from random import randint

attempts = 0
pc = randint(0, 10)
print('\nSou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
player = int(input('Seu palpite: '))

while player != pc:
    attempts += 1
    if player > pc:
        print('\nMenos... Tente novamente.')
        player = int(input('Seu palpite: '))
    elif player < pc:
        print('\nMais... Tente novamente.')
        player = int(input('Seu palpite: '))

print('\nAcertou com {} tentativas.\nPARABÉNS!'.format(attempts + 1))
