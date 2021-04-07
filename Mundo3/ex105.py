def grades(* values, sit = False):
    List = dict()
    List['total'] = len(values)
    List['maior'] = max(values)
    List['menor'] = min(values)
    List['média'] = sum(values) / len(values)
    
    if sit == True:
        if List['média'] < 6:
            List['situação'] = 'RUIM'
        else:
            List['situação'] = 'BOA'
         
    return List


answer = grades(5.5, 2.5, 1.5, sit = True)
print(answer)