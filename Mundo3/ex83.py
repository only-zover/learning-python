ex = str(input('Digite uma expressão: '))
stack = []

for symb in ex:
    if symb == '(':
        stack.append('(')
    elif symb == ')':
        if len(stack) > 0:
            stack.pop()
        else: 
            stack.append(')')
            break

if len(stack) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
