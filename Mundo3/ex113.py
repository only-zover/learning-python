def readint(text):
    while True:
        try:
            n = int(input(text))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro.')
            continue
        except KeyboardInterrupt:
            print('O usuário interrompeu o processo.')
            return 0
        else:
            return n
            

def readfloat(text):
    while True:
        try:
            n = float(input(text))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário interrompeu o processo.')
            return 0
        else: 
            return n


n = readint('Digite um inteiro: ')
m = readfloat('Digite um float: ')
print(f'Você acabou de digitar o número {n} e {m}.')             