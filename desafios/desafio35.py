r1 = float(input('Digite a medida da primeira reta em cm: '))
r2 = float(input('Digite a medida da segunda reta em cm: '))
r3 = float(input('Digite a medida da terceira reta em cm: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo')
