from desafios.desafio109 import moeda
dinheiro = float(input('Digite o valor: R$'))
print(f'A metade é {moeda.metade(dinheiro, show=True)}')
print(f'O dobro desse valor é {moeda.dobro(dinheiro, show=False)}')
print(f'Aumentado o valor em 10%, temos {moeda.aumento(dinheiro, 10, show=True)}')
print(f'Diminuindo o valor em 30%, temos {moeda.diminuir(dinheiro, 30, show=True)}')
