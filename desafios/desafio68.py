from random import randint
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
pontuacao = 0
while True:
    print('-=-' * 10)
    escolha_n = int(input('Escolha um número de 0 a 10 | Número: '))
    escolha_pi = ' '
    while escolha_pi not in 'PI':
        escolha_pi = str(input('Escolha [P] Par [I] Ímpar | Opção: ')).strip().upper()
    print('---' * 10)
    comp = randint(0, 10)
    resultado = comp + escolha_n
    print(f'O computador escolheu {comp}. O resulado é {resultado}!')
    print('---' * 10)
    if resultado % 2 == 0:
        if escolha_pi == 'P':
            print(f'Portanto você ganhou! Parabéns!')
            print('Vamos jogar novamente...')
            pontuacao += 1
        elif escolha_pi == 'I':
            print(f'Portanto você perdeu! :(')
            break
    else:
        if escolha_pi == 'I':
            print(f'Portanto você ganhou! Parabéns!')
            print('Vamos jogar novamente...')
            pontuacao += 1
        elif escolha_pi == 'P':
            print(f'Portanto você perdeu! :(')
            break
print(f'O JOGO ACABOU! Você venceu {pontuacao} vezes!')
