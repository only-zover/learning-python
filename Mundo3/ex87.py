matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = c3 = b2l = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Declare [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            even += matriz[l][c]
        if c == 2:
            c3 += matriz[l][c]
        if l == 1:
            b2l = matriz[l][c]
            if matriz[l][c] > b2l:
                b2l = matriz[l][c]
        
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
            
print(f'\nA soma dos valores pares: {even}.\nA soma dos valores da terceira coluna: {c3}.\nO maior valor da segunda linha: {b2l}.\n')
