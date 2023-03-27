from datetime import date
maior = 0
menor = 0
for pergunta in range (0, 7, 1):
    nasc = int(input('Qual o ano de nascimento da pessoa: '))
    idade = date.today().year - nasc
    if (idade >= 18):
        maior = maior + 1
    else:
        menor = menor + 1
print('Há {} pesoas de menor e {} de maior'.format(menor, maior))