def Help(command):
    help(command)


command = ''

while True:
    command = str(input('Função ou Biblioteca > ')).strip()
    if command.upper() == 'FIM':
        break
    else: 
        Help(command)
    