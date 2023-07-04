from datetime import datetime


def voto(ano_nasc):
    idade = datetime.today().year - ano_nasc
    print(f'Com {idade} anos: ', end='')
    if 18 <= idade < 70:
        return 'VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade >= 70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO NEGADO'


print('-'*20)
print(voto(int(input('Ano de Nascimento: '))))
