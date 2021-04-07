from modules import coin

n = float(input('Digite o preço: R$'))


print(f'A metade de {coin.coin(n)} é {coin.half(n, True)}')
print(f'O dobro de {coin.coin(n)} é {coin.double(n, True)}')
print(f'Aumentando 10%, temos {coin.increase(10, n, True)}')
print(f'Reduzindo 13%, temos {coin.decrease(13, n, True)}')