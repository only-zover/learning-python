name = str(input('Digite seu nome: ')).strip()
splitName = name.split()

print('Seu primeiro nome é {}, o seu último nome é {}.'.format(splitName[0], splitName[len(splitName) - 1]))
