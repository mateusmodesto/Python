lista = ['cachorro quente', 'lanche', 'suco', 'pudim']
print(lista)
# formas de mudar a baixo
lista.append('banana')  # .append adiciona itens à lista!
print(lista)
lista[2] = 'coca'
print(lista)
lista.insert(2, 'picolé')
print(lista)
# modo de ordem:
numeros = [1, 4, 8, 2, 5]
print(numeros)
numeros.sort()
print(numeros)
numeros.sort(reverse=True)  # coloca em ordem decrescente
print(numeros)
# formas de remover itens:
numeros.pop()  # pop remove o último item
print(numeros)
numeros.pop(2)  # remove o 2° itens
print(numeros)
numeros.remove(2)  # caso tenha dois números iguais, ele remove apenas o primeiro que estiver  na ordem
print(numeros)
# mostrar quantidade de elementos:
print(f'Essa lista tem {len(numeros)} elementos')
print('---'*20)
valores = [ ]
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
