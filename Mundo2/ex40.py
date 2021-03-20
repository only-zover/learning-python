n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))

avarage = (n1 + n2) / 2
text = ''

if avarage < 5:
    text = '{:.1f}\nReprovado.'
elif 7 > avarage >= 5:
    text = '{:.1f}\nEstá de recuperação...'
else:
    text = '{:.1f}\nParabéns!\nAprovado!'

print(' ')
print('Sua média é:', text.format(avarage))
print(' ')
