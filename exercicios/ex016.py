lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])
print(lanche[0:3])
print(lanche[2:])
print(lanche[:2])
print(lanche)
print(len(lanche))
print('--'*20)
#TULAS SÃO IMUTÁVEIS
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('--'*20)
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('--' * 20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
print('--'*20)
print(sorted(lanche)) #coloca em ordem alfabética
print('--'*20)
a = (2, 5, 8)
b = (5, 8, 1, 2)
c = b + a
d = a + b
#b+a != a+b
print(c)
print(d)
print(c.count(5))  #quantas vezes está aparacendo o número 5
print(c.index(8))  #em que posição está o 8
print('--'*20)
pessoa = ('Mateus', 14, 'M', 53)
print(pessoa)
del(pessoa)  #não pode deletar apenas os itens da tupla, APENAS A TUPLA INTEIRA!
