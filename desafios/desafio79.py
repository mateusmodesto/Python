lista = []
while True:
    n1 = int(input('Digite um valor: '))
    if n1 not in lista:
        print('Número digitado com sucesso!')
        lista.append(n1)
    else:
        print('Número já existente!')
    resp = str(input('Você quer continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break
lista.sort()
print(f'Os números digitados foram {lista}')