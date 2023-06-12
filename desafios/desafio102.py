def fatorial(num=0, show=False):
    f = 1
    for a in range(num, 0, -1):
        f *= a
        if show:
            return print(f'{a} x', end='')
        else:
            return f


print(fatorial(int(input('Digite um número para calcular: ')), bool(input('Quer mostrar o processo? [True/False]: '))))
