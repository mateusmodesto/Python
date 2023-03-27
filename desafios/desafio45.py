from random import choice
from time import sleep
print('--'*30)
print('Seja Bem-Vindo ao jogo Pedra, Papel e Tesoura!')
print('--' * 30)
escolha = input('Suas opções: [Pd] Pedra [Pp] Papel [T] Tesoura  ')
cpu = choice(['Pd', 'Pp', 'T'])
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if cpu == 'Pp':
    if escolha == 'T':
        print('A máquina escolheu Papel, portanto você perdeu!!')
    elif escolha == 'Pd':
        print('A máquina escolheu Papel, portanto você GANHOU!')
    elif escolha == 'Pp':
        print('A máquina escolheu Papel, portanto houve um EMPATE!!')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 'T':
    if escolha == 'Pp':
        print('A máquina escolheu Tesoura, portanto você perdeu!!')
    elif escolha == 'Pd':
        print('A máquina escolheu Tesoura, portanto você GANHOU!')
    elif escolha == 'T':
        print('A máquina escolheu Tesoura, portanto houve um EMPATE!!')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 'Pd':
    if escolha == 'Pp':
        print('A máquina escolheu Pedra, portanto você perdeu!!')
    elif escolha == 'T':
        print('A máquina escolheu Pedra, portanto você GANHOU!')
    elif escolha == 'Pd':
        print('A máquina escolheu Pedra, portanto houve um EMPATE!!')
    else:
        print('JOGADA INVÁLIDA')
