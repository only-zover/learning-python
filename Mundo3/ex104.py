def ReadInt(text):
   ok = False
   value = 0
   while True:
      n = str(input(text))
      if n.isnumeric():
         value = int(n)
         ok = True
      else:
         print('ERRO!')
      if ok:
         break
   return value
   
n = ReadInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')    