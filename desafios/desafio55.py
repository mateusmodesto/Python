maior = 0
menor = 0
for a in range(0, 5):
    peso = float(input('Digite o peso  da pessoa: '))
    if peso >= maior:
        maior = peso
    else:
        if menor == 0:
            menor = peso
        elif menor > peso:
            menor = peso
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))
