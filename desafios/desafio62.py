n = int(input('Digite um número: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))
termos = int(input('Gostaria de mostrar quantos termos? '))
arit = 0
while termos != 0:
    while arit <= termos - 1:
        print(n)
        n += razao
        arit += 1
    arit = 0
    termos = int(input('Quantos termos gostria de mostrar a mais? '))
