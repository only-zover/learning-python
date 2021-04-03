from datetime import date

data = {}

data['Nome'] = str(input('Nome: '))
born = int(input('Ano de nascimento: '))
data['Idade'] = date.today().year - born
data['CTPS'] = int(input('Carteira de trabalho (0 = não tem): '))

if data['CTPS'] != 0:
    data['Contratação'] = int(input('Ano de contratação: '))
    data['Salário'] = float(input('Salário: R$'))
    data['Aposentadoria'] = (data['Contratação'] - born) + 35

print()
for k, v in data.items():
    print(f'{k} tem o valor {v}.')
print()