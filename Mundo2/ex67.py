while True:
    n = int(input('\nTabuada do: '))
    
    if n < 0:
        break
    
    for x in range(1, 10):
        print(f'{n} x {x} = {x * n}')

print('Fim')
