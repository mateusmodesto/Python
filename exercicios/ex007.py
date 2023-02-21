import random
name1 = str(input('Digite o nome do 1° jogador: '))
name2 = str(input('Digite o nome do 2° jogador: '))
name3 = str(input('Digite o nome do 3° jogador: '))
name4 = str(input('Digite o nome do 4° jogador: '))
comecar = random.choice([name1, name2, name3, name4])
print('O Jogador que vai começar primeiro vai ser: {}'.format(comecar))
resp = str(input('Gostaria de jogar o dado? [1]SIM [2]NÃO '))
if resp == str(1):
    number = random.randint(1, 6)
    print('O número sorteado foi {}'.format(number))
