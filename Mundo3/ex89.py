file = list()

while True:
    name = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    avarage = (n1 + n2) / 2
    
    file.append([name, [n1, n2], avarage])
    
    end = ' '
    while end not in 'SN':
        end = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if end == 'N':
        break
    
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

for i, a in enumerate(file):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    
while True:
    choose = int(input('\nVerificar qual aluno: (999 para sair) '))
    
    if choose == 999:
        break
    
    if choose <= len(file) - 1:
        print(f'Notas de {file[choose][0]} são {file[choose][1]}')
        