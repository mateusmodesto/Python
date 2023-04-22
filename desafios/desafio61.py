n = int(input('Digite um número para ser o primeiro termo: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))
arit = 1
while arit <= 10:
    print('{} -> '.format(n), end='')
    n += razao
    arit += 1
print('FIM')