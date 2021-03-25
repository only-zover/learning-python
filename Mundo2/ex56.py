s = 0
old = 0
oldName = ''
sub20tw = 0

for x in range(1, 5):
    print('----- {}ª PESSOA -----'.format(x))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()

    if x == 1 and sex in 'Mm':
        old = age
        oldName = name
    if age > old and sex in 'Mm':
        old = age
        oldName = name
    
    if sex == 'F' and age < 20:
        sub20tw += 1

    s += age

print('\nA média de idade do grupo é de {} anos.\nO homem mais velho é {} com {} anos.\nAo todo são {} mulheres com menos de 20 anos.\n'.format(s / 4, oldName, old, sub20tw))
