from random import randint
from time import sleep
jogadores = dict()
geral = list()
print('Valores Sorteados: ')
for i in range(0, 4):
    jogadores[f'jogador{i+1}'] = randint(1, 6)
    sleep(1)
    print(f'Jogador {i+1} sorteou o número {jogadores[f"jogador{i+1}"]}')
print('Raking dos Jogadores:')
pos = 0
for num in sorted(jogadores, key=jogadores.get, reverse=True):
    pos += 1
    sleep(1)
    print(f'{pos}° lugar: {num} com {jogadores[num]}')
