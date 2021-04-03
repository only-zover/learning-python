filme = {
    'título': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values()) # 'Star Wars', 1997, 'George Lucas'
print(filme.keys())   # 'título', 'ano', 'diretor'
print(filme.items())  # ('título', 'Star Wars'), ('ano', '1997'), ('diretor', 'George Lucas')

print()

for k, v in filme.items(): # O título é Star Wars
    print(f'O {k} é {v}.') # etc.
    