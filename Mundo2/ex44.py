value = float(input('Digite o preço do produto: R$'))
print(' ')
print('Escolha a forma de pagamento.')
print(' ')
Type = int(input('[ 1 ] À vista (dinheiro/cheque)\n[ 2 ] À vista (cartão)\n[ 3 ] Em até 2x no cartão\n[ 4 ] 3x ou mais no cartão\n\nSua escolha: '))
if Type < 1 or Type > 4:
    exit('ERRO!\nDigite um valor válido (1, 2, 3, 4).')

off10 = value - (value * 0.1)
off5 = value - (value * 0.05)
plus20 = value + (value * 0.2)
method = ''
text = ''
portionText = ''

if Type == 1:
    value = off10
    method = 'À vista (dinheiro/cheque)'
    text = '10% de desconto'
elif Type == 2: 
    value = off5
    method = 'À vista (cartão)'
    text = '5% de desconto'
elif Type == 3:
    value
    method = 'Em até 2x no cartão'
    text = 'Sem alteração no preço'
    portionText = 'Sua compra será parcelada em 2x de R${:.2f}.'.format(value / 2)
elif Type == 4:
    value = plus20
    method = '3x ou mais no cartão'
    text = '20% de juros cobrados'
    portion = int(input('\nEscolha a quantidade de parcelas: '))
    if portion < 3:
        exit('ERRO!\nA quantidade de parcelas deve ser maior ou igual a 3.')
    else:
        portionText = 'Sua compra será parcelada em {}x de R${:.2f}.'.format(portion, value / portion)

print(' ')
print('-'*65)
if portionText:
    print(portionText)
print('Você escolheu o método de pagamento: {}.\n{}!\nO valor final do seu produto é R${:.2f}'.format(method, text, value))
print('-'*65)
