name = str(input('Seu nome: '))

splitName = name.split()
noSpaceName = name.replace(' ', '')
 
print('#'*60)
print('Caixa alta: {}\nCaixa baixa: {}\nnº de caracteres: {}\nnº de caracteres do 1º nome: {}'
.format(name.upper(), name.lower(), len(noSpaceName), len(splitName[0])))
print('#'*60)
