resp = ''
soma = menor = maior = numeros = 0
while resp != 'N':
    n1 = int(input('Digite um número inteiro: '))
    soma += n1
    if numeros == 1:
        meior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
    numeros += 1
    resp = str(input('VocÊ gostaria de continuar? [S] Sim [N] Não \n Opção: ')).upper()
media = soma/numeros
print('A media entre todos os números digitados foi {}'.format(media))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
