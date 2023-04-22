n = int(input('Digite um número inteiro: '))
sqc = 0
atual = 1
antigo = -1
while sqc < n:
    fibonacci = antigo + atual
    antigo = atual 
    atual = fibonacci
    sqc += 1
    print('{} -> '.format(fibonacci), end='')
print('FIM')
