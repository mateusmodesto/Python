from datetime import date
ano = int(input('Digite o ano (Caso queira selecionar o ano atual selecione 0): '))
if ano == 0:
    ano = date.today().year
if ano%4==0 and ano % 100 != 0 or ano % 400 == 0:
    print('É um ano Bissexto')
else:
    print('Não é um ano Bissexto')