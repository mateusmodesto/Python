def area(larg, compri):
    a = larg * compri
    print(f'A área do terreno {larg}x{compri} é de {a}m²')


print(' CONTROLE DE TERRENOS  ')
print('-' * 23)
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
