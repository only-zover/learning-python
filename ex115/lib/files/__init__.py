from lib.interface import *

def fileexist(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def createfile(file):
    try:
        a = open(file, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {file} criado com sucesso!')
        

def readfile(file):
    try:
        a = open(file, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        header('PESSOAS CADASTRADAS')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        a.close()
    

def register(file, name='Unknown', age=0):
    try:
        a = open(file, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('Houve um erro na digitação dos dados!')
        else:
            print(f'Novo registro de {name} adicionado.')
