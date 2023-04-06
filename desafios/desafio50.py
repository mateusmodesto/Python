soma = 0
for a in range (0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print('A soma de todos os números pares digitados é {}'.format(soma))
