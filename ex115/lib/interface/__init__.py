def line(size=42):
    return '-'*size
 
 
def header(text):
    print(line())
    print(text.center(42))
    print(line())
    
    
def readint(text):
    while True:
        try:
            n = int(input(text))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro.')
            continue
        except KeyboardInterrupt:
            exit('O usuário interrompeu o processo.')
        else:
            return n


def menu(catalog):
    header('MENU PRINCIPAL')
    c = 1
    for item in catalog:
         print(f'{c} - {item}')
         c += 1
    print(line())
    op = readint(('Sua opção: '))
    return op
        


