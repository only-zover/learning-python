values = list()

for cont in range(0, 5):
    values.append(int(input('Digite um valor: ')))
              
print(f'\nVocê digitou os valores: {values}.')
print(f'\nO maior valor digitado é {max(values)} nas posições: ', end = '')

for i, v in enumerate(values):
    if v == max(values):
        print(f'{i+1}...', end = '')

print(f'\nO menor valor digitado é {min(values)} nas posições: ', end = '')

for i, v in enumerate(values):
    if v == min(values):
        print(f'{i+1}...', end = '')
        