from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
m_m = sorted(lista)
print(f'Os números sorteados foram: {lista}')
#print(f'O maior número sorteado foi {m_m[0]}')
print(f'O maior número sorteado foi {max(lista)}')
print(f'O menor número sorteado foi {min(lista)}')
