def File(name = '<desconhecido>', points = 0):
    print(f'O jogador {name} fez {points} ponto(s) no campeonato.')


name = str(input('\nNome do jogador: ')).strip()
points = str(input('Número de pontos: ')).strip()

if points.isnumeric():
    points = int(points)
else:
    points = 0
        
if name == '':
    File(points = points)
else:
    File(name, points)
