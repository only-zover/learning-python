adult = men = wom = 0
while True:
    age = int(input('Idade: '))
    
    if age >= 18:
        adult += 1
         
    sex = ' '
    while sex not in 'mMfF':
        sex = str(input('Sexo: [M/F] ')).strip()[0]
        
    if sex in 'mM':
        men += 1
    if sex in 'fF' and age < 20:
        wom += 1
              
    end = ' '
    while end not in 'sSnN':
        end = str(input('Quer continuar? [S/N] ')).strip()[0]
    
    if end in 'nN':
        break

print(f'\nO total de maiores de idade é {adult}.\nAo todo temos {men} homens cadastrados.\nE temos {wom} mulheres com menos de 20 anos.\n')
