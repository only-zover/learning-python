player = dict()
matches = list()

player['name'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {player["name"]} jogou? '))

for p in range(0, total):
    matches.append(int(input(f'Quantos pontos na partida {p + 1}? ')))
    
player['points'] = matches[:]
player['total'] = sum(matches)
 
print(player)
print()

for k, v in player.items():
    print(f'O campo {k} tem o valor {v}.')

print()

print(f'O jogador {player["name"]} jogou {total} partidas.')
for i, v in enumerate(player['points']):
    print(f'    Na partida {i}, fez {v} pontos.')
print(f'\nUm total de {player["total"]} pontos.')
