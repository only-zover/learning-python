v = float(input('Preço: R$'))
off5 = (v * 0.05)
vF = v - off5
print('Promoção: de R${:.2f} por R${:.2f}! 5%OFF'.format(v, vF)) 
