geral = list()
estatisticas = dict()
gols = list()
while True:
    total = 0
    print('--'*20)
    estatisticas['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas o {estatisticas["nome"]} jogou? '))
    for part in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {part}? '))
        total += gol
        gols.append(gol)
    estatisticas['gols'] = gols[:]
    estatisticas['total'] = total
    gols.clear()
    geral.append(estatisticas.copy())
    while True:
        resp = str(input('Quer add mais jogador? [S/N] ')).upper()
        if resp in 'SN':
            break
        else:
            print('ERROR')
    if resp == 'N':
        break
print('-=-'*20)
print('cod ', end='')
for i in estatisticas.keys():
    print(f'{i:<15}', end='')
print()
print('--'*20)
for p, i in enumerate(geral):
    print(f'{p:>3} ', end='')
    for r in i.values():
        print(f'{str(r):<15}', end='')
    print()
print('--'*20)
while True:
    resp = int(input('Digite o código do jogador para mais inf: (999 para): '))
    if resp == 999:
        break
    elif resp >= len(geral):
        print('Número é inválido!')
    else:
        print(f'Levantamento do {geral[resp]["nome"]}: ')
        for p, g in enumerate(geral[resp]['gols']):
            print(f' => No jogo {p+1} fez {g} gols')
        print('--' * 20)
