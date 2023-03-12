lado1 = float(input('Digite a medida do lado 1: '))
lado2 = float(input('Digite a medida do lado 2: '))
lado3 = float(input('Digite a medida do lado 3: '))
if lado1 != lado2 != lado3 and lado1 != lado3:
    print('Triângulo Escaleno!!!')
elif lado1 == lado2 == lado3:
    print('Triângulo Equilátero!!!')
else:
    print('Triângulo Isóceles!!!')