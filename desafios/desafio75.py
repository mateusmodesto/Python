lista = (int(input('Digite um número inteiro: ')),
         int(input('Digite um número inteiro: ')),
         int(input('Digite um número inteiro: ')),
         int(input('Digite um número inteiro: ')))
print(lista)
print(f'Foi digitado {lista.count(9)} vezes o número 9')
if 3 in lista:
    print(f'O primeiro três foi digitado na posição: {lista.index(3)+1}')
else:
    print('O número 3 não foi digitado!')
par = 0
print(f'Os números pares digitados são: ', end='')
for i in lista:
    if i % 2 == 0:
        par += 1
        print(i, ' ', end='')
if par == 0:
    print('Nenhum número foi digitado!')
