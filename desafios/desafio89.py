grupo = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    notas1 = float(input('Digite a nota 1 do aluno: '))
    notas2 = float(input('Digite a nota 2 do aluno: '))
    resp = str(input('Você quer continuar? [S/N] ')).upper()
    media = (notas1 + notas2) / 2
    grupo.append([nome, [notas1, notas2], media])
    if resp == 'N':
        break
print('-=-'*11)
print(f'No.  {"NOME":^7} {"MÉDIA":^17}')
print('--'*15)
for p in grupo:
    print(f'{grupo.index(p)} {p[0]:^14} {p[2]:^10}')
while True:
    num = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
    if num == 999:
        break
    print(f'As notas do {grupo[num][0]} são: {grupo[num][1]}')
print('Programa Finalizando....')
