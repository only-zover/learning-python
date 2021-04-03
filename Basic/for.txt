''' for ... in range(..., ...):
    ...
'''
# for x in range(0, 6):  Contando de 0 até 5
#     print(x)
# print('FIM')

# for x in range(6, 0, -1):  Contando de 6 até 1
#     print(x)
# print('FIM')

# for x in range(0, 6, 2):  Contando de 0 até 5 de 2 em 2
#     print(x)
# print('FIM')

# Example

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for x in range(i, f+1, p):
    print(x)
print('FIM')