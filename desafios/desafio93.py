estatisticas = dict()
gols = list()
total = 0
estatisticas['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas o {estatisticas["nome"]} jogou? '))
for part in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {part}? '))
    total += gol
    gols.append(gol)
estatisticas['gols'] = gols[:]
estatisticas['total'] = total
print('-=-'*25)
print(estatisticas)
print('-=-'*25)
for item, valor in estatisticas.items():
    print(f'{item} tem o valor {valor}')
print('-=-'*25)
print(f'O jogador {estatisticas["nome"]} jogou {partidas} partidas: ')
for part, gol in enumerate(gols):
    print(f' => Na partida {part}, fez {gol} gols')
