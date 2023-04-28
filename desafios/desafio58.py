from random import randint
print('Sortiei um número. Tente Adivinhar!')
numero = randint(0, 10)
tentativas = 0
acertou = False
while not acertou:
    resp = int(input('Digite o número que foi sorteado: '))
    if resp < numero:
        print('Você errou!')
        print('O número é maior')
    elif resp > numero:
        print('Você errou!')
        print('O número é menor')
    elif resp == numero:
        acertou = True
    tentativas += 1
print('Você acertou! Parabéns! Você conseguiu na {}° tentativa!'.format(tentativas))
