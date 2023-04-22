n1 = int(input('Digite um número inteiro: '))
soma = 0
vezes = 0
while n1 != 999:
    soma += n1
    n1 = int(input('Digite outro número: '))
    vezes += 1
print('Foram digitados {} números. A soma de todos é {}'.format(vezes, soma))
