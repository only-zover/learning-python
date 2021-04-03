student = dict()

student['Nome'] = str(input('Nome: '))
student['Média'] = float(input(f'Média de {student["Nome"]}: '))
student['Situação'] = 'Aprovado'

if student['Média'] < 6:
    student['Situação'] = 'Reprovado'
    

for k, v in student.items():
    print(f'{k} é igual a {v}.')
