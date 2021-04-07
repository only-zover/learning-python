def vote(born):
    from datetime import date
    age = date.today().year - born
    text = f'Com {age} anos: VOTO '
    if age < 16:
        text += 'NEGADO'
    elif age < 18 or age >= 65:
        text += 'OPCIONAL'
    else:
        text += 'OBRIGATÓRIO'
    return text


born = int(input('Em que ano você nasceu? '))
print(vote(born))
