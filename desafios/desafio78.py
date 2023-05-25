lista = []
for i in range(0, 5):
    n1 = int(input('Digite um número: '))
    lista.append(n1)
menor = min(lista)
maior = max(lista)
print(f'O menor valor da lista é {menor} na posição ', end='')
for posicao, numero in enumerate(lista):
    if numero == menor:
        print(f'{posicao}... ', end='')
print(f'\nO maior valor da lista é {maior} na posição ', end='')
for posica, numero in enumerate(lista):
    if numero == maior:
        print(f'{posica}...', end='')

