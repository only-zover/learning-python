h = float(input('Digite sua altura: '))
w = float(input('Digite seu peso: '))

imc = w / (h ** 2)
level = ''

if imc < 18.5:
    level = 'abaixo do peso'
elif imc < 25:
    level = 'no peso ideal'
elif imc < 30:
    level = 'com sobrepeso'
elif imc < 40:
    level = 'com obesidade'
else:
    level = 'com obesidade mórbida'

print(' ')
print('Seu IMC é de {:.1f}.\nVocê está {}.'.format(imc, level))
print(' ')
