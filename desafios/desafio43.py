peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
IMC = peso / (altura * altura)
if IMC < 18.5:
    print('Seu IMC é {:.3f}, portanto você está Abaixo do peso!!'.format(IMC))
elif IMC < 25:
    print('Seu IMC é {:.3f}, portanto você está Peso ideal'.format(IMC))
elif IMC < 30:
    print('Seu IMC é {:.3f}, portanto você está Sobrepeso'.format(IMC))
elif IMC < 40:
    print('Seu IMC é {:.3f}, portanto você está com Obesidade'.format(IMC))
else:
    print('Seu IMC é {:.3f}, portanto você está com Obesidade mórbida'.format(IMC))
