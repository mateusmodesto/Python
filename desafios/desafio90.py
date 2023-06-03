aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
for titulo, valor in aluno.items():
    print(f'{titulo} é igual a {valor}')
