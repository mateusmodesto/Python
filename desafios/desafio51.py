n = int(input('Digite um número: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))
decimo = n + 10 * razao
print('Os dez primeiros termos dessa progressão são: ')
for arit in range (n, decimo, razao):
    print(arit)

