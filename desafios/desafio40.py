n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1+n2)/2
if media < 5.0:
    print('Sua média foi {}, portanto você está REPROVADO!!!'.format(media))
elif 5.0 <= media < 7:
    print('Sua média foi {}, portanto você está de RECUPERAÇÃO!!!'.format(media))
else:
    print('Sua média foi {}, portanto você está APROVADO'.format(media))