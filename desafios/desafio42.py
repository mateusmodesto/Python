lado1 = float(input('Digite a medida do lado 1: '))
lado2: float = float(input('Digite a medida do lado 2: '))
lado3 = float(input('Digite a medida do lado 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado3:
    print('É possível formar um triângulo')
    if lado1 != lado2 != lado3 != lado1:
        print('Triângulo Escaleno!!!')
    elif lado1 == lado2 == lado3:
        print('Triângulo Equilátero!!!')
    else:
        print('Triângulo Isóceles!!!')
else:
    print('Não é possível formar um triângulo!!')