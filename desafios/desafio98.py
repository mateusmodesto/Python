from time import sleep


def contador(i, f, p):
    print('-='*20)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        while i <= f:
            print(i, end=' ', flush=True)
            sleep(0.5)
            i += p
    else:
        while i >= f:
            print(i, end=' ', flush=True)
            sleep(0.5)
            i -= p

    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Ínicio: ')), int(input('Fim: ')), abs(int(input('Passo: '))))
