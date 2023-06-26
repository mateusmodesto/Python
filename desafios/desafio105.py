def notas(*num, sit=False):
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
    if sit:
        if media >= 7:
            print('BOA')
        elif media >= 5:
            print('RAZOÁVEL')
        else:
            print('RUIM')
    print(menor)
    print(maior)
    print(quantidade)
    print(media)


notas(5.5, 6.4, 7.8, 5.6, 9, 8, sit=True)
