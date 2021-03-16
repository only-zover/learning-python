h = float(input('Height? '))
w = float(input('Width? '))
a = int(h * w)
pPm = 2
l = int(a / pPm)
print('A parade tem {0}m² e serão necessários {1}L de tinta para pinta-lá.'.format(a, l))
