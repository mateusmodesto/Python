from time import sleep
from random import randint
num = list()

    
def sorteia(lista):
    print('Os números sorteados foram: ', end='')
    for n in range(0, 5):
        sor = randint(1, 10)
        lista.append(sor)
        print(sor, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO !')


def soma(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {num} temos {s}')


sorteia(num)
soma(num)
