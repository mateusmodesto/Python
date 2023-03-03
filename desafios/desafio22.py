nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('O total de caracteres do seu nome é {}'.format(len(nome)-nome.count(' ')))
print('O total de caracteres do seu primeiro nome é {}'.format(len(dividido[0])))

