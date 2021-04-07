def ReadMoney(text):
    ok = False
    
    while True:
        
        while not ok:
            entry = str(input(text)).replace(',','.').strip()
        
            if entry.isalpha() or entry == '':
                print('ERRO!')
            else:
                ok = True
                return float(entry)
    

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