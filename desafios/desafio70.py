total = mais_de_1000 = menor_v = 0
barato_p = ' '
print('--'*10)
print('{: ^20}'.format('SUPER LOJÃO'))
while True:
    print('--'*10)
    print('PRODUTO SENDO CADASTRADO')
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto R$'))
    total = total + preco
    if preco > 1000:
        mais_de_1000 += 1
    if menor_v == 0:
        menor_v = preco
        barato_p = produto
    elif preco < menor_v:
        barato_p = produto
    print('--' * 10)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Há mais produtos para adicionar? [S] Sim [N] Não | Opção: ')).upper().strip()[0]
    if resp == 'N':
        break
print('--'*30)
print(f'O total de gasto foi R${total :.2f}')
print(f'Foi registrado(s) {mais_de_1000} produto(s) que custam mais de R$1000')
print(f'O nome do produto mais barato registrado foi o(a) {barato_p}')
