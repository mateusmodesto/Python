n1 = int(input('Digite um número para calcular o fatorial: '))
fat = 1
while n1 > 0:
    print('{}'.format(n1), end='')
    print(' x ' if n1 > 1 else ' = ', end='')
    fat = fat * n1
    n1 -= 1
print('{}'.format(fat))
