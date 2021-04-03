from random import randint

num = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'\nOs valores sorteados foram: ', end = '')
for n in num:
    print(n, end = ' ')
print(f'\nO maior valor é {max(num)}.\nO menor valor é {min(num)}\n')
