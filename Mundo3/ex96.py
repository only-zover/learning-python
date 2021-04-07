def area(a, b):
    print(f'A área do terreno {a}x{b} é {a*b:.1f}m².')


print('CONTROLE DE TERRENOS')

w = float(input('LARGURA (m): '))
h = float(input('ALTURA (m): '))

area(w, h)
