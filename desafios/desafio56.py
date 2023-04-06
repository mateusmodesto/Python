velho = 0
soma = 0
mulher20 = 0
nomevelho = ''
for a in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo (F ou M): ')).upper()
    soma = soma + idade
    if sexo == "M":
        if idade > velho:
            velho = idade
            nomevelho = nome
    if sexo == "F":
        if idade < 20:
            mulher20 = mulher20 + 1
media = soma / 4
print('A média de idade desse grupo é {:.1f} anos'.format(media))
print('O homem mais velho é o {}'.format(nomevelho))
print('Há {} mulher(es) com menos de 20 anos'.format(mulher20))
