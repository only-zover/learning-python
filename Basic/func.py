# def sum(a, b):
#     s = a + b
#     print(s)
    
    
# sum(4, 1)

# def contador(* num):
#     size = len(num)
#     print(f'Recebi os valores {num}, ao todo são {size} números.')
    
# contador(2, 1)
# contador(1, 2, 3)
# contador(5, 4, 1, 0)

# valores = [2 , 1, 3, 5, 9, 0]

# def dobrar(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
# dobrar(valores)
# print(valores)
 
 
def sum(* values):
    s = 0
    for num in values:
        s += num    
    print(f'Somandos os valores {values} temos {s}.')

sum(1, 2, 5)
