sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
while sexo != 'MASCULINO' and sexo != 'FEMININO':
    print('erro')
    sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
print('Entendido!')
