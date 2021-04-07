def factorial(num=1, show=False):
    f = 1
    for c in range(num, 1, -1):
        if show == True:
            print(c, end = '' )
            if c > 2:
                print(' x ', end = '')
            else:
                print(' = ', end = '')

        f *= c
        
    return f


print(factorial(5))
