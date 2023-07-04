from time import sleep
c = ('\033[m', '\033[0;30;41m', '\033[1;30;43m', '\033[0;30;46m', '\033[7;30m')


def titulo(mensagem, cor=0):
    numero = len(mensagem)+4
    print(c[cor], end='')
    print('~'*numero)
    print(f'{mensagem: ^{numero}}')
    print('~'*numero)
    print(c[0], end='')
    sleep(1)


def funcao(comando, cor=0):
    print(c[cor], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    n = input('Função ou Biblioteca > ')
    if n.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        titulo(f'Acessando o manual do comando "{n}"', 3)
        funcao(n, 4)
