d = float(input('A distância em km da sua viagem: '))

fastTravel = d / 2
travel = d * 0.45

if d <= 200:
    print('Viagem curta...\nSua viagem de {}km custará R${:.2f}!'.format(d, fastTravel))
else:
    print('Viagem comum...\nSua viagem de {}km custará R${:.2f}!'.format(d, travel))

# travel = d / 2 if d <= 200 else d * 0.45 - Maneira simplificada
