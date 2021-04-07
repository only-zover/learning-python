from modules import coin

n = float(input('Digite o preço: R$'))

print(f'A metade de {n} é {coin.half(n)}')
print(f'O dobro de {n} é {coin.double(n)}')
print(f'Aumentando 10%, temos {coin.increase(10, n)}')
