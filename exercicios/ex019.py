pessoas = {'nome': 'Mateus', 'idade': 15, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')


print('--'*10)


print(pessoas.keys())  # para mostrar os títulos de cada item
print('--'*10)
print(pessoas.values())  # para mostrar os valores de cad a item
print('--'*10)
print(pessoas.items())  # para mostrar tanto os títulos quanto os valores
print('--'*10)


for k in pessoas.keys():
    print(k)
print('--'*10)


for k in pessoas.values():
    print(k)
print('--'*10)


for k, v in pessoas.items():
    print(f'{k} = {v}')
print('--'*10)


# PARA APAGAR:
del pessoas['sexo']
print(pessoas)
print('--'*10)


# PARA TROCAR:
pessoas['idade'] = 18
print(pessoas)
print('--'*10)


# PARA ADICIONAR:
pessoas['peso'] = 53.5
print(pessoas)
print('--'*10)


estado1 = {'uf': 'São Paulo', 'sigla': 'Sp'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'Rj'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
