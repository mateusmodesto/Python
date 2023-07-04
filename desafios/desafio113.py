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


def leiaFloat(msg):
    n = 0
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('\033[0;31m ERRO: por favor digite um número real válido! \033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31m ERRO: O usuário não digitou o número real! \033[m')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
