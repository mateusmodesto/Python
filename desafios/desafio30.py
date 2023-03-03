num = int(input('Digite um número inteiro: '))
paim = num % 2
if paim == 0:
    print('{} é um número par' .format(num))
else:
    print('{} é um número ímpar'.format(num))