def increase(rate, value=0, formato=False):
    total = value + (value * rate / 100)
    return total if not formato else coin(total) 

    
def decrease(rate, value=0, formato=False):
    total = value - (value * rate / 100)
    return total if not formato else coin(total) 
    

def double(value=0, formato=False):
    total = value * 2
    return total if not formato else coin(total) 
    
    
def half(value=0, formato=False):
    total = value / 2
    return total if not formato else coin(total) 


def coin(value=0, sign ='R$'):
    return f'{sign}{value:>.2f}'.replace('.', ',')


def resume(value=0, valueIncrease=0, valueDecrease=0):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{coin(value)}')
    print(f'Dobro do preço: \t{double(value, True)}')
    print(f'Metade do preço: \t{half(value, True)}')
    print(f'{valueIncrease}% de aumento: \t{increase(valueIncrease, value, True)}')
    print(f'{valueDecrease}% de redução: \t{decrease(valueDecrease, value, True)}')
    print('-'*30)
    