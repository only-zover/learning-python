import math

a = float(input('Insira um ângulo: '))
sen = math.sin(math.radians(a))
cos =  math.cos(math.radians(a))
tg = math.tan(math.radians(a)) 
print('O valor é {}º\nSeno: {:.2f}º\nCosseno: {:.2f}º\nTangente: {:.2f}º.'.format(a, sen, cos, tg))
