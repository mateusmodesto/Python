nome = str(input('Qual o seu nome? '))
print('Bom Dia, {}!'.format(nome))
casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos gostaria de parcelar? '))
prestacao = casa / (anos * 12)
porcentagem = salario * 0.30
if prestacao > porcentagem:
    print('O empréstimo foi negado, por execeder 30% do salário!')
else:
    print('O valor da parcela ficou R${:.2f}'.format(prestacao))