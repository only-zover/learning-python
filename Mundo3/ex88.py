from random import randint

lucky = int(input('Quantos jogos: '))
num_list = list()

for c in range(0, lucky):
    for n in range(1,7):
        
        r = randint(1, 60)

        if r not in num_list:
            num_list.append(r)
            
    print(f'Jogo {c}: {num_list}')
    num_list.clear()
