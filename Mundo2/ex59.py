from time import sleep


v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
op = 0

while op != 5:
    print('\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair\n')
    op = int(input('Sua escolha: '))
    sleep(0.6)

    if op == 5:
        off = True
    
    elif op == 4:
        v1 = int(input('Primeiro Valor: '))
        v2 = int(input('Segundo valor: '))
    
    elif op == 3:
        if v1 > v2:
            big = v1
        else:
            big = v2
        print('Entre {} e {}, o maior é {}.'.format(v1, v2, big))
    
    elif op == 2:
        print('{} x {} = {}'.format(v1, v2, v1 * v2))
    
    elif op == 1:
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    
    else:
        print('Insira um valor válido.')
    sleep(0.6)

print('Finalizando...'), sleep(0.8), print('Programa encerrado.\n')
