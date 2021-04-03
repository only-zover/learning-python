player = dict()
everyone = list()
matches = list()

while True:
    player.clear()
    matches.clear()
    
    player['name'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {player["name"]} jogou? '))

    for m in range(0, total):
        matches.append(int(input(f'    Quantos pontos na {m + 1}ª partida? ')))
    
    player['points'] = matches[:]
    player['total'] = sum(matches)
    
    everyone.append(player.copy())
    
    while True:
        end = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if end in 'SN':
            break
        print('ERRO! Por favor digite apenas "S" ou "N".')
        
    if end == 'N':
        break
    
print()
print('Cód. ', end = '')
for i in player.keys():
    print(f'{i:<15}', end = '')
print()    
for k, v in enumerate(everyone):
    print(f'{k+1:>4} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()

while True:        
    while True:
        who = int(input(f'Mostrar dados de qual jogador? (999 para parar)'))
        if who > 0 and who <= len(everyone) or who == 999:
            break
        print('ERRO! Insira um valor válido.')
        
    print(f'\nLevantamento do jogador {everyone[who - 1]["name"]}:')
    for i, m in enumerate(everyone[who - 1]['points']):
        print(f'    No jogo {i + 1} fez {m} pontos')
    print()
    
    if who == 999:
        break