person = dict()
everyone = list()
AgeSum = 0

while True:
    person.clear()
    person['name'] = str(input('Nome: ')).strip()
    
    while True:
        person['sex'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if person['sex'] in 'MF':
            break
        print('ERRO! Por favor digite apenas "M" ou "F".')
    
    person['age'] = int(input('Idade: '))
    AgeSum += person['age']
    
    everyone.append(person.copy())
    
    while True:
        end = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if end in 'SN':
            break
        print('ERRO! Por favor digite apenas "S" ou "N".')
            
    if end == 'N':
        break

avarage = AgeSum / len(everyone)

print(f'''
A) Ao todo temos {len(everyone)} pessoas cadastradas.
B) A média de idade é {avarage:5.2f} anos.
C) As mulheres cadastradas foram.
''', end = '')
for p in everyone:
    if p['sex'] == 'F':
        print(f'{p["name"]} ', end = '')
print(f'\nD) Lista das pessoas que estão acima da média:')
for p in everyone:
    if p['age'] > avarage:
        print(f'    {p["name"]}, {p["age"]} anos')
