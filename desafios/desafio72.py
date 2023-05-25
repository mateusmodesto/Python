contagem = ("zero", 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', "oito", 'nove',
            'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
            'vinte')
while True:
    n1 = int(input('Digite um número inteiro entre 0 e 20: '))
    if n1 < 0 or n1 > 20:
        n1 = int(input('Digite outro número inteiro entre 0 e 20: '))
    elif 0 <= n1 <= 20:
        print(f'Você digitou o número {contagem[n1]}')
    resp = str(input('Você quer continuar? ')).upper()
    if resp == 'N':
        break
    elif resp =='S':
        continue
