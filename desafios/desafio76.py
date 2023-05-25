lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90)
print('--'*20)
print(f'{"LISTA DE COMPRA":^40}')
print('--'*20)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:.2f}')
