grupo = list()
pessoas = list()
leves = list()
pesados = list()
total = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    grupo.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    total += 1
    if resp == 'N':
        break
menor = maior = grupo[0][1]
leves.append(grupo[0][0])
pesados.append(grupo[0][0])
for p in grupo:
    if maior <= p[1]:
        if maior < p[1]:
            pesados.clear()
        maior = p[1]
        pesados.append(p[0])
for m in grupo:
    if menor >= m[1]:
        if menor > m[1]:
            leves.clear()
        menor = m[1]
        if m[0] not in leves:
            leves.append(m[0])
print(f'O maior peso foi {maior}Kg. De {pesados}')
print(f'O menor peso foi {menor}Kg. De {leves}')
 