phrase = str(input('Digite uma frase: ')).upper().strip()

print(' ')
print('A letra "A" aparece {} vezes na frase.\nA primeira letra "A" aparece na posição {}.\nA última letra "A" aparece na posição {}.'.format(phrase.count('A'), phrase.find('A') + 1, phrase.rfind('A') + 1))
print(' ')
