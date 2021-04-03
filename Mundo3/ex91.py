from time import sleep
from random import randint
from operator import itemgetter

players = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

ranking = list()

print('\nValores sorteados:')
for k, v in players.items():
    print(f'    O {k} tirou {v}!')
    sleep(0.8)
print('\nRanking dos jogadores: ')

ranking = sorted(players.items(), key = itemgetter(1), reverse = True) # THIS

for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.8) 
