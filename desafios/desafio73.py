contagem = ('Fluminense', 'Botafogo', 'Fortaleza', 'Palmeiras', 'Vasco da Gama', 'Internacional', 'Bragantino',
            'Flamengo', 'São Paulo', 'Goiás', 'Athletico-PR', 'Cruzeiro', 'Grêmio', 'Corinthans', 'Cuiabá',
            'Atlético-Mg', 'Santos', 'Bahia', 'Coritiba', 'América-MG')
print('{:-^41}'.format('TABELA DO BRASILEIRÃO'))
print(contagem)
print('--'*21)
print(f'Os 5 primeiros colocados {contagem[0:5]}')
print('--'*21)
print(f'Times do Rebaixamento: {contagem[16:20]}')
print('--'*21)
print(f'Tabela dos times em ordem Alfabética: {sorted(contagem)}')
print('--'*21)
colocacao = contagem.index('Palmeiras')
print(f'O Palmeiras está em {colocacao+1}º Lugar')
