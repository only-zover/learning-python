name = str.lower(input('Seu nome: '))

splitName = name.split()
silvaCheck = splitName.count('silva')

if silvaCheck >= 1:
    print('Seu nome possui Silva.')
else:
    print('Seu nome não possui Silva.')

# name = str(input('Seu nome')).strip()
# print('Seu nome possui Silva? {}'.format('silva' in name.lower()))