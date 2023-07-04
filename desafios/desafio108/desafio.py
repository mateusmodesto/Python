from desafios.desafio108 import moeda
dinheiro = float(input('Digite o valor: R$'))
print(f'A metade é {moeda.moeda(moeda.metade(dinheiro))}')
print(f'O dobro desse valor é {moeda.moeda(moeda.dobro(dinheiro))}')
print(f'Aumentado o valor em 10%, temos {moeda.moeda(moeda.aumento(dinheiro, 10))}')
print(f'Diminuindo o valor em 30%, temos {moeda.moeda(moeda.diminuir(dinheiro, 30))}')
