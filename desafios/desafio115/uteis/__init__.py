def leiaInt(msg):
    n = 0
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[0;31m ERRO: por favor, digite um número inteiro válido! \033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31m ERRO: O usuário não digitou o número inteiro! \033[m')
            return 0
        else:
            return n


def titulo(msg):
    print('--'*15)
    print(f'{msg}'.center(30))
    print('--'*15)


def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print('--'*15)
    return leiaInt('\033[0;33m Sua Opção: \033[m')



