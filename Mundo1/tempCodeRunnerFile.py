days = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual foi a distância em quilômetros(Km) percorrida pelo carro? '))
total = (days * 60.00) + (km * 0.15)
print('O total a se pagar é de R${:.2f}'.format(total))
