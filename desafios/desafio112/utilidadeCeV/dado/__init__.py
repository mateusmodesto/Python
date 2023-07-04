def leiaDinheiro(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mEscreva um preço válido!!!\033[m')
        else:
            valido = True
            return float(entrada)
