from datetime import date
ano = int(input('Em qual ano você nasceu? '))
idade = date.today().year - ano
if idade < 18:
    print('De acordo com sua idade, você ainda se alistará no serviço militar!')
    falta = 18 - idade
    print('Faltam {} anos para se alistar!'.format(falta))
elif idade > 18:
    print('Já passou o tempo para se alistar ao serviço militar!!!')
    falta = idade - 18
    print('Já se passaram {} anos do seu tempo para alistar!!'.format(falta))
else:
    print('De acordo com sua idade, já está na hora de se alistar para o exército!!')