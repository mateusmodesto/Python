grupo = list()
alunos = list()
notas = list()
while True:
    alunos.append(str(input('Digite o nome do aluno: ')))
    notas.append(float(input('Digite a nota 1 do aluno: ')))
    notas.append(float(input('Digite a nota 2 do aluno: ')))
    alunos.append(notas[:])
    grupo.append(alunos[:])
    resp = str(input('Você quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
    notas.clear()
    alunos.clear()
print(grupo)
print('-=-'*11)
print(f'No.  {"NOME":^7} {"MÉDIA":^17}')
print('--'*15)
for p in grupo:
    media = (p[1][0] + p[1][1])/2
    print(f'{grupo.index(p)} {p[0]:^14} {media:^10}')
num = 0
while True:
    num = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
    if num == 999:
        break
    print(f'As notas do {grupo[num][0]} são: {grupo[num][1]}')
print('Programa Finalizando....')
