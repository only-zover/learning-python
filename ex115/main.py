from lib.interface import *
from lib.files import *
from time import sleep

file = 'log.txt'

if not fileexist(file):
    createfile(file)
else:
    print('Arquivo não encontrado!')

while True:
    reply = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    
    if reply == 1:
        readfile(file)
    elif reply == 2:
        header('NOVO CADASTRO')
        name = str(input('Nome: '))
        age = readint('Idade: ')
        register(file, name, age)
    elif reply == 3:
        header('Saindo...')
        break      
    else:
        print('Opção inválida!')
    sleep(1)