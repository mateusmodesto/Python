nome = str(input('Qual o seu nome? '))
if nome == 'Mateus':
    print('Que nome bonito!')
elif nome == 'Enzo' or nome == 'Ana':
    print('Se nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))