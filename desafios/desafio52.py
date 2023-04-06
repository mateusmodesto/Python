vezes = 0
n1 = int(input('Digite um número inteiro: '))
for divisivel in range (1, n1 + 1):
    if n1 % divisivel == 0:
        vezes = vezes+1
if vezes == 2:
    print('O {} é primo'.format(n1))
else:
    print('O {} não é primo!'.format(n1))