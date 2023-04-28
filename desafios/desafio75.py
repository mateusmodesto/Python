for c in range(0, 4):
    num = int(input('Digite um número inteiro: '))
    if c == 0:
        num1 = num
    elif c == 1:
        num2 = num
    elif c == 2:
        num3 = num
    elif c == 3:
        num4 = num
    c += 1
lista = (num1, num2, num3, num4)
print(lista)
if 9 in lista:
    print(f'Foi digitado {lista.count(9)} vezes o número 9')
if 3 in lista:
    print(f'O primeiro três foi digitado na posição (de 0 a 3): {lista.index(3)}')
par = 0
r = lista[0]
for i in range (0, len(lista)):
    print(r)
    if r % 2 == 0:
        par += 1
    r = lista[0+1]
print(f'Foram digitados {par} números pares')


