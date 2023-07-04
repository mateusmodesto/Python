def diminuir(num=0, menos=0, show=False):
    '''
        --> Diminuir o valor
    :param num: valor que será utilizado para calcular
    :param menos: porcentagem que diminuirá o num
    :param show: valor opcional, caso verdadeiro, irá formatar o valor
    :return: valor final
    '''
    res = num*menos/100
    return res if show is False else moeda(res)


def aumento(num=0, mais=0, show=False):
    '''
        --> Calcula aumento
    :param num: valor que será utilizado para calcular
    :param mais: porcentagem que aumentará o valor
    :param show: valor opcional, caso verdadeiro, irá formatar o valor
    :return: valor final
    '''
    res = num+num*mais/100
    return res if show is False else moeda(res)


def metade(num=0, show=False):
    '''
        --> Calcula a metade do valor
    :param num: valor que será utilizado para calcular
    :param show: valor opcional, caso verdadeiro, formatará o valor final
    :return: valor final
    '''
    res = num/2
    return res if show is False else moeda(res)


def dobro(num=0, show=False):
    '''
        --> Calcula o dobro do valor
    :param num: valor que será calculado
    :param show: valor opcional, se verdadeiro, formatará o valor final
    :return: valor final
    '''
    res = num*2
    return res if show is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    '''
        --> Formata o valor
    :param preco: valor
    :param moeda: moeda que formatará
    :return: valor formatado
    '''
    return f'{moeda}{preco:.2f}'.replace('.', ',')
