a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

text = ''

if b > a:
    text = 'O segundo valor é o maior.\n{} < {}'
elif a == b:
    text = 'Os valores são iguais.\n{} = {}'
else:
    text = 'O primeiro valor é maior.\n{} > {}'
print('-='*11)
print(text.format(a, b))
print('-='*11)
