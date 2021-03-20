from datetime import date

born = int(input('Digite seu ano de nascimento: '))

today = date.today().year
age = today - born
text = ''
plu = 'anos'

if age == 17 or age == 19:
    plu = 'ano'

print('Quem nasceu em {} tem {} anos em {}.'.format(born, age, today))

if age == 18:
    text = 'Você tem que se alistar imediatamente!'
elif age < 18:
    text = 'Faltam {} {} para o alistamento.'.format(18 - age, plu)
else:
    text = 'Você deveria ter se alistado {} {} atrás.'.format(age - 18, plu)
print(' ')
print(text)
print(' ')
