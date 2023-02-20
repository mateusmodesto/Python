dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (dias*60) + (km*0.15)
print('O aluguel do carro custou R${:.2f}'.format(valor))
