soma = 0
vezes = 0
while True:
    n1 = int(input('Digite outro número: '))
    vezes += 1
    if n1 == 999:
        break
    soma += n1
print(f'Foram digitados {vezes} números. A soma deles vale {soma}!')
