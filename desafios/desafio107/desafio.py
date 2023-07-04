from desafios.desafio107 import moeda
dinheiro = float(input('Digite o valor: R$'))
print(f'A metade é R${moeda.metade(dinheiro)}')
print(f'O dobro desse valor é R${moeda.dobro(dinheiro)}')
print(f'Aumentado o valor em 10%, temos R${moeda.aumento(dinheiro, 10)}')
print(f'Diminuindo o valor em 30%, temos R${moeda.diminuir(dinheiro, 30)}')