V = float(input('A velocidade atual (km/h): '))

maxV = 80
multa = (V - maxV) * 7

print(' ')
if V > maxV:
    print('Limite de velocidade ultrapassado!\nMulta de R${:.2f}'.format(multa))
else:
    print('Ok!')
print(' ')
    