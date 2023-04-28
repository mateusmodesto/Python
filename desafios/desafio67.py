while True:
    tabuada = int(input('Digite um valor para calcular a tabuada: '))
    if tabuada >= 0:
        print('-'*25)
        for cont in range (1,11):
            resultado = cont * tabuada
            print(f'{tabuada} x {cont} = {resultado} ')
        print('-' * 25)
    else:
        break
print('TABUADA ENCERRADA! Volte sempre!')