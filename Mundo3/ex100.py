from random import randint
from time import sleep

numbers = list()


def Draws(List):
    print('Sorteando 5 valores...', end = '')
    for c in range(0, 5):
        n = randint(1, 10)
        numbers.append(n)
        print(f'{n}', end = ' ')
        sleep(0.3)
    print('FIM!')
          

def SumEven(List):
    s = 0
    for n in List:
        if n % 2 == 0:
            s += n    
    print(f'Somando os valores pares de {List}, temos {s}.')


Draws(numbers)
SumEven(numbers)
