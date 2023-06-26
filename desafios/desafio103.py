def ficha(nome, gols):
    if nome == '':
        nome = '< desconhecido >'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s)')


ficha(str(input('Digite o nome: ')), str(input('Gols marcados: ')))
