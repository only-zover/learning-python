phrase = str(input('Digite uma frase: ')).strip().upper()

text = 'não é'
words = phrase.split()
inverted = phrase[::-1]
together = ''.join(words)

if together == inverted:
    text = 'é'
print('\nO inverso de "{}" é "{}".\nA frase digitada {} um palíndromo.\n'.format(together, inverted, text))    
