a = int(input('Digite o lado "a" do triângulo: '))
b = int(input('Digite o lado "b" do triângulo: '))
c = int(input('Digite o lado "c" do triângulo: '))

text = 'Não é possível formar um triângulo com os lados {1}, {2} e {3}.'
tType = 'isóceles'

if c < a + b and b < a + c and a < b + c:
    text = 'É possível formar um triângulo {0} com os lados {1}, {2} e {3}.'

if a == b == c:
    tType = 'equilátero'
elif a != b != c != a:
    tType = 'escaleno'

print(' ')
print(text.format(tType, a, b, c))
print(' ') 
