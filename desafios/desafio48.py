soma = 0
for impar in range (1, 501, 2):
    if impar % 3 == 0:
        soma += impar
print('A soma dos números ímpares entre 1 e 500 e que são múltiplos de 3 é {}'.format(soma))