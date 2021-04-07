from modules import coin

n = float(input('Digite o preço: R$'))


print(f'A metade de {coin.coin(n)} é {coin.coin(coin.half(n))}')
print(f'O dobro de {coin.coin(n)} é {coin.coin(coin.double(n))}')
print(f'Aumentando 10%, temos {coin.coin(coin.increase(10, n))}')
