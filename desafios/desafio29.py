velocidade = float(input('Digite a velocidade atual do carro em km/h: '))
if velocidade > 80:
    multa = (velocidade - 80)*7.00
    print('Você foi multado e o valor é R${:.2f}'.format(multa))
else:
    print('Você estava dentro da velocidade máxima')
