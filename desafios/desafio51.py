n = int(input('Digite um número: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))
print('Os dez primeiros termos dessa progressão são: ')
for arit in range (n, razao*10, razao):
    print(arit)
