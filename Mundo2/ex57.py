sex = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]

while sex not in 'FM':
   sex = str(input('Dados inválidos! Por favor, informeu seu sexo: [M/F] ')).strip().upper()[0]

if sex == 'F':
   sex = 'FEMININO'
elif sex == 'M':
   sex = 'MASCULINO'

print('\nSexo {} registrado com sucesso.\n'.format(sex))
