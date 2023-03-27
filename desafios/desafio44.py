preco = float(input('Qual o preço do produto? R$'))
forma = input('Qual a forma de pagamento? [1] Dinheiro/cheque [2] Á vista no cartão '
              '[3] 2x no Cartão [4] 3x no Cartão \nForma: ')
if forma == '1':
    preco = preco * 0.90
    print('O preço com desconto ficou R${}'.format(preco))
elif forma == '2':
    preco = preco * 0.95
    print('O preço com desconto ficou R${}'.format(preco))
elif forma == '3':
    print('O preço ficou R${}'.format(preco))
    parcela = preco / 2
    print('Cada parcela ficou R${:.2f}'.format(parcela))
elif forma == '4':
    preco = preco * 1.20
    parcela = int(input('Quantas vezes gostaria de parcelar? '))
    parcela = preco / parcela
    print('O preço ficou R${}'.format(preco))
    print('Cada parcela ficou R${:.2f}'.format(parcela))
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente!')