maior = homens = mulher_menor = 0
while True:
    print('--'*15)
    print('CADASTRE UMA PESSOA')
    print('--' * 15)
    idade = int(input('Insira a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Insira o sexo da pessoa [M] Masculino [F] Feminino | Opção: ')).upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Gostaria de cadastrar mais pessoas? [S] Sim [N] Não | Opção: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Houve {maior} pessoas de maior cadastradas!')
print(f'Houve {homens} homens cadastrados!')
print(f'Houve {mulher_menor} mulheres que tem menos de 20 anos cadastradas!')
