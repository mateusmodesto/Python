import random
from time import sleep
num1 = random.randint(0, 5)
print('-=-' * 20)
resp = int(input('Tente acertar qual foi o número inteiro escolhido entre 0 e 5: '))
print('-=-' * 20)
print('Processando...')
sleep(3)
if resp == num1:
    print('Parabéns você acertou!')
else:
    print('Que Pena, você não acertou!')
    print('O número escolhido foi {}'.format(num1))
