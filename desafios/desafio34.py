salario = float(input('Digite o valor do seu salário: '))
if salario > 1250.00:
    novo = salario * 1.10
    print('O seu novo salário será R${:.2f}'.format(novo))
else:
    novo = salario * 1.15
    print('O seu novo salário será R${:.2f}'.format(novo))
