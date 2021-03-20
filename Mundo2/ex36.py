value = float(input('Insira o valor da casa: R$'))
wage = float(input('Insira o seu salário: R$'))
years = int(input('Insira em quantos anos vai pagar: '))

installment = value / (years * 12)
limit = wage * 0.30

print(' ')
if installment > limit:
    print('A prestação será de: R${:.2f}\nValor: R$ {:.2f}\nSalário: R$ {:.2f}\nAnos: {}\n\nEmpréstimo negado!'.format(installment, value, wage, years))
else: 
    print('A prestação será de: R${:.2f}\nValor: R$ {:.2f}\nSalário: R$ {:.2f}\nAnos: {}\n\nEmpréstimo bem-sucedido!'.format(installment, value, wage, years))
print(' ')
