valor = int(input('Digite o valor que será sacado R$'))
valortotal = valor
cedula = 50
total_cedula = 0
while True:
    if valortotal >= cedula:
        valortotal -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if valortotal == 0:
            break