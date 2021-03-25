n = int(input('Digite um número inteiro: '))
total = 0
isPrime = False
text = 'Não é'

for x in range(1, n + 1):
    if n % x == 0:
        total += 1

if total == 2:
    isPrime = True
    text = 'É'

print('\nO número {} é divisível por {} valores.\n{} um número primo.\n'.format(n, total, text))
