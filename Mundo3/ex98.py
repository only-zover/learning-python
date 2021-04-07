from time import sleep


def counter(start, end, step):
    stepstr = step
    endtext = end
    
    if step == 0:
        step = 1
        
    print('-='*20)
    
    if start > end:
        step *= -1
        end -= 2
        stepstr = str(step)[1]
    
    print(f'Contagem de {start} até {endtext}, de {stepstr} em {stepstr}.') 
        
    for n in range(start, end + 1, step):
        print(f'{n}', end = ' ')
        sleep(0.4)
    print('FIM!')
        
        
counter(1, 10, 1)
counter(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')

start = int(input('Ínicio: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

counter(start, end, step)
