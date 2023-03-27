from datetime import date
ano = int(input('Em que ano o atleta nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('Este atleta é da categoria MIRIM')
elif idade <= 14:
    print('Este atleta é da categoria INFANTIL')
elif idade <= 19:
    print('Este atleta é da categoria JUNIOR')
elif idade <= 25:
    print('Este atleta é da categoria SÊNIOR')
else:
    print('Este atleta é da categoria MASTER')