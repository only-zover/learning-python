n = c = s = 0

while True:
    n = int(input('Digite um número: [999 para parar] '))
    
    if n == 999:
        break
    
    s += n
    c += 1

print(f'\nA soma dos {c} valores é {s}.\n')
