def fatorial(num=0, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: número para calcular a fatorial
    :param show: operador para verificar se o usuário quer que mostre a conta
    :return: resultado da fatorial
    """
    f = 1
    for a in range(num, 0, -1):
        f *= a
        if show:
            print(f' x {a}', end=' ')
            if a == num - (num - 1):
                print('= ', end='')
    return f


help(fatorial)
print(fatorial(int(input('Digite um número para calcular: ')), bool(input('Quer mostrar o processo? [True/False]: '))))
