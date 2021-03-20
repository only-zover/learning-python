from datetime import date

born = int(input('Digite o ano do seu nascimento: '))

today = date.today().year
age = today - born
text = 'Você tem {} anos.\nÉ um nadador de nível {}!'

if age < 10:
    level = 'Mirim'
elif age < 15:
    level = 'Infantil'
elif age < 20:
    level = 'Junior'
elif age < 26:
    level = 'Sênior'
else:
    level = 'Master'

print(' ')
print(text.format(age, level))
print(' ')
