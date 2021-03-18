name = str.lower(input('Insira seu nome: '))

splitName = name.split()
firstName = splitName[0]
haveSanto = firstName.count('santo') 


if haveSanto == True:  
    print('Seu nome começa com Santo')
else: 
    print('Seu nome não começa com Santo')

# name = str(input('Insira seu nome: ')).strip()

# print(name[:5].upper() == 'SANTO')