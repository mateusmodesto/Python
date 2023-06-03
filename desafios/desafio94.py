pessoa = dict()
conjunto = list()
soma = 0
while True:

    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO!')

    conjunto.append(pessoa.copy())

    while True:
        resp = str(input('Quer adicionar mais pessoas? [S/N] ')).upper()
        if resp in 'NS':
            break
    if resp == 'N':
        break
print(f'- Foram cadastradas {len(conjunto)} pessoas')
print('-=-'*20)
print('- As mulheres cadastradas foram: ', end='')
for i in conjunto:
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')
    soma += i['idade']
media = soma/len(conjunto)
print(f'\n- A média de idade é {media}')
print('- O pessoal com a idade a cima da média são: ')
for i in conjunto:
    if i['idade'] >= media:
        for k, j in i.items():
            print(f'{k} = {j}; ', end='')
        print()
