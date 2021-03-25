big = 0
low = 0

for x in range(1, 6):
    weight = float(input('Peso da {}º pessoa: '.format(x)))
    if x == 1:
        big = weight
        low = weight
    else:
        if weight > big:
            big = weight
        if weight < low:
            low = weight

print('\nO maior peso é {} kg.\nO menor peso é {} kg.'.format(big, low))
