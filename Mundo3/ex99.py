def bigger(* values):
    bigger = 0
    c = 0
    for v in values:
        c += 1
        if c == 1:
            bigger = v
        if v > bigger:
            bigger = v
            
    print('Analisando os valores passados...')
    
    for v in values:
        print(f'{v}', end = ', ')
    print(f'Foram informados {c} valores ao todo.\nMaior valor informado: {bigger}')
            
bigger(1, 2, 6, 5)
bigger(6)
bigger(99, 1, 52, 1)
