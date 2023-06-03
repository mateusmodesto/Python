def mostralinha():
    print('-' * 30)


def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'{a} + {b} = {s}')


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números')


def somaup(*num):
    s = 0
    for valor in num:
        s += valor
    print(f'Somando os números: {num} temos {s}')


def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# PROGRAMA PRINCIPAL
mostralinha()
print('     CURSO EM VÍDEO      ')
mostralinha()
mostralinha()
print('   CADASTRO DE FUNCIONÁRIOS      ')
mostralinha()
mostralinha()
print('     ERRO NO SISTEMA      ')
mostralinha()
# ---------------------------------------------------
mensagem('      CURSO EM VÍDEO      ')
mensagem('      PYTHON É BOM        ')
mensagem('            OLÁ           ')
#  --------------------------------------------------
soma(4, 5)
soma(8, 9)
soma(2, 1)
# ---------------------------------------------------
contador(1, 4, 5, 6)
contador(4, 8)
contador(6, 9, 1, 5, 2, 8)
# ---------------------------------------------------
valores = [7, 2, 5, 0, 4]
dobrar(valores)
print(valores)
# ---------------------------------------------------
somaup(4, 5, 2)
somaup(1, 2)
