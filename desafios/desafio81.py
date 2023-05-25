lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? (S/N) ')).upper()
    if resp[0] == 'N':
        break
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')
if 5 in lista:
    print(f'Foi digitado o número 5!')
else:
    print('Não foi digitado o número 5!')
