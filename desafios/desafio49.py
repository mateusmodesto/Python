n = int(input('Digite o número inteiro, que queira saber a tabuada: '))
result = 0
print('{} TABUADA {}'.format('-=-'*2, '-=-'*2))
for tabuada in range(1, 11):
    result = n * tabuada
    print('     {} x {} = {}'.format(n, tabuada, result))
print('-=-'*8)