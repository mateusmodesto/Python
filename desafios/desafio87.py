tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma_1 = 0
for l in range(0, 3):
    for c in range(0, 3):
        tabela[l][c] = int(input(f'Digite uma valor {l, c}: '))
print('-=-'*10)
maior = tabela[1][0]
for l in range(0, 3):
    soma_1 += tabela[l][2]
    for c in range(0, 3):
        print(f'[{tabela[l][c]:^5}]', end='')
        if tabela[l][c] % 2 == 0:
            soma += tabela[l][c]
        if maior < tabela[1][c]:
            maior = tabela[1][c]
    print()
print('-=-'*10)
print(f'A soma de todos os pares é {soma}')
print(f'A soma dos números da última coluna é {soma_1}')
print(f'O maior valor da segunda linha é {maior}')
