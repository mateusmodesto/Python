numeros = list()
pares = list()
impares = list()
for a in range(0, 7):
    numeros.append(int(input('Digite um número: ')))
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Os números pares digitados são: {sorted(pares)}')
print(f'OS números ímpares digitados são: {sorted(impares)}')
