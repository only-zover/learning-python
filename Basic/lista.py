num = [2, 7, 9, 1]

num[2] = 3 # Troca o valor do índice 2 pelo valor 3.

num.append(7) # Adiciona o valor 7 no índice final.

num.sort(reverse=True) # num.sort - Coloca os valores em ordem crescente. # reserse = True - inverte a ordem do comando. (ordem decrescente)

num.insert(2, 1) # Insere o valor 1 no índice 2, deslocando pra frente os índices 2 e maiores.

num.pop() # Elimina o índice final. O valor dentro do parênteses é o índice a ser eliminado.

num.remove(2) # Elimina o primeiro valor.

print(num)
print(max(num))
print(len(list(str(min(num)))))