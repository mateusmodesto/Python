soma = 0
vezes = 0
while True:
    n1 = int(input('Digite outro número: '))
    if n1 == 999:
        break
    soma += n1
    vezes += 1
print(f'Foram digitados {vezes} números. A soma deles vale {soma}!')