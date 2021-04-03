vogais = ('a', 'e', 'i', 'o', 'u')

word = str(input('Digite uma palavra: ')).strip()

v = ''

for letter in word:
    if letter.lower() in 'aeiou':
        v += letter

print(f'As vogais são: {v}')