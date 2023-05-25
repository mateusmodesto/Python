from random import randint
j = a = 0
palpite = list()
print(f'--'*20)
print(f'{"MEGA SENA":^40}')
print(f'--'*20)
quanti = int(input('Quantos jogos você quer que sorteie? '))
while j < quanti:
    j += 1
    while a < 6:
        num = randint(0, 60)
        if num not in palpite:
            palpite.append(num)
            a += 1
    print(f'Jogo {j}: {palpite}')
    palpite.clear()
    a = 0
