contagem = ("zero", 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', "oito", 'nove',
            'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
            'vinte')
n1 = int(input('Digite um número inteiro entre 0 e 20: '))
while n1 < 0 or n1 > 20:
    n1 = int(input('Digite outro número inteiro entre 0 e 20: '))
    if 0 <= n1 <= 20:
        break
print(f'Você digitou o número {contagem[n1]}')
