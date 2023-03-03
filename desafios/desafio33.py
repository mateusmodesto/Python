n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2:
    if n2 > n3:
        print('O maior número é {}'.format(n1))
        print('O menor número é {}'.format(n3))
    else:
        if n1 > n3:
            print('O maior número é {}'.format(n1))
            print('O menor número é {}'.format(n2))
        else:
            print('O maior número é {}'.format(n3))
            print('O menor número é {}'.format(n2))
else:
    if n1 > n3:
        print('O maior número é {}'.format(n2))
        print('O menor número é {}'.format(n3))
    else:
        if n2 > n3:
            print('O maior número é {}'.format(n2))
            print('O menor número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n3))
            print('O menor número é {}'.format(n1))
