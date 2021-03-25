n = int(input('Fatorial: '))
r = 1
c = n

while c > 1:
    r *= c 
    c -= 1
    
print('\nCalculando...\n{}! = {}.\n'.format(n, r))


# FOR

# for x in range(n, 1, -1):
#     r *= c
#     c -= 1

# print(r)