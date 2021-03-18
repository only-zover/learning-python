import math

# a = (co ** 2 + ca ** 2) **(1/2)

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
a = math.hypot(co, ca)
print('O comprimento da hipotenusa é de {:.2f}'.format(a)) 
