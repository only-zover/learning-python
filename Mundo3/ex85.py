num = [[], []]

for c in range(1, 8):
    v = (int(input(f'Digite o {c}º valor: ')))
    
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)
        
num[0].sort()
num[1].sort()

print(f'\nOs valores pares digitados: {num[0]}.\nOs valores ímpares digitados: {num[1]}.\n')
