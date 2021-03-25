s = 0
cont = 0

for x in range(1, 501, 2): # o passo 2 ajuda a diminuir as iterações caso usasse if x % 2 != 0:
    if x % 3 == 0:
        cont += 1
        s += x
print('A soma {} valores, tem como resultado {}.'.format(cont, s))
