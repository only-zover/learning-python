wage = float(input('Digite seu salário: R$'))

newWage = wage + (wage * 0.15)
qui = '15%'

if wage > 1250:
   newWage = wage + (wage * 0.10)
if wage > 1250:
    qui = '10%' 
   
print('Aumento de {}!\nSeu salário aumentou de R${:.2f} para R${:.2f}.'.format(qui, wage, newWage))
