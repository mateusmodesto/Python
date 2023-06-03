import datetime
dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
dicionario['idade'] = datetime.date.today().year - anonasc
dicionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['ctps'] != 0:
    dicionario['anocontratacao'] = int(input('Ano de Contratação: '))
    dicionario['salario'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = (dicionario['anocontratacao'] - anonasc) + 35
print('-=-'*10)
for t, v in dicionario.items():
    print(f'{t} tem o valor {v}')
