from datetime import datetime


def voto(ano_nasc):
    idade = datetime.today().year - ano_nasc
    print(f'Com {idade} anos: ', end='')
    if (idade >= 18) and (idade < 70):
        return print('VOTO OBRIGATÓRIO')
    elif ((idade >= 16) and (idade < 18)) or (idade >= 70):
        return print('VOTO OPCIONAL')
    else:
        return print('VOTO NEGADO')


print('-'*20)
voto(int(input('Ano de Nascimento: ')))
