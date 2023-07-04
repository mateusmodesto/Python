def notas(*num, sit=False):
    """
    -> Função para analisar as notas e situação de uma classe.
    :param num: aceitar a digitação das notas dos alunos (mais de um valor aceito)
    :param sit: valor opcional para mostrar o valor da situção da média dos alunos.
    :return: mostra um dicionário com a quantidade, maior, menor, media (notas) e situação da media.
    """
    sala = dict()
    quantidade = soma = 0
    maior = menor = num[1]
    for i in num:
        if i > maior:
            maior = i
        elif menor > i:
            menor = i
        quantidade += 1
        soma += i
    media = soma / quantidade
    sala['quantidade'] = quantidade
    sala['maior'] = maior
    sala['menor'] = menor
    sala['media'] = media
    if sit:
        if media >= 7:
            sala['situação'] = 'BOA'
        elif media >= 5:
            sala['situação'] = 'RAZOÁVEL'
        else:
            sala['situação'] = 'RUIM'
    return sala


print(notas(5.5, 2.5, 1.5, sit=True))
help(notas)
