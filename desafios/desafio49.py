n = int(input('Digite o número inteiro, que queira saber a tabuada: '))
for tabuada in range(1, 11):
    print('{} x {} = {}'.format(n, tabuada, n * tabuada))
