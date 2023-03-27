maior = 0
menor = 0
for a in range(0, 2):
    peso = float(input('Digite o peso  da pessoa: '))
    if peso >= maior:
        maior = peso
    else:
        if menor == 0:
            menor = peso

print(maior)
print(menor)
