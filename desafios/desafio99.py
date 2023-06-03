from time import sleep


def maior(*num):
    m = cont = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for i in num:
        print(i, end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            m = i
        else:
            if i > m:
                m = i
        cont += 1
    print(f'Foram informados {cont} números')
    print(f'O maior valor é {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
