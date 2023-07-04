def diminuir(num=0, menos= 0):
    return num*menos/100


def aumento(num=0, mais=0):
    return num+num*mais/100


def metade(num=0):
    return num/2


def dobro(num=0):
    return num*2


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

