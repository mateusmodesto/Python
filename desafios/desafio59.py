n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
resp = 0
while resp != 5:
    print('==' * 10)
    resp = int(input('''Escolha uma das opções abaixo: 
     [1] somar        [4] novos números
     [2] multiplicar  [5] sair
     [3] maior \n Opção: '''))
    print('==' * 10)
    if resp == 1:
        print('  {} + {} = {}'.format(n1, n2, n1 + n2))
    elif resp == 2:
        print('  {} * {} = {}'.format(n1, n2, n1*n2))
    elif resp == 3:
        if n1 > n2:
            print('{} é o maior número digitado'.format(n1))
        else:
            print('{} é o maior número digitado'.format(n2))
    elif resp == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
print('SAIU')
