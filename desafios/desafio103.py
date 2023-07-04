def ficha(nome, gols):
    if nome == '':
        nome = '< desconhecido >'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s)')


ficha(str(input('Digite o nome: ')).strip(), str(input('Gols marcados: ')).strip())
