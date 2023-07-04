import asyncore


def arquExiste(nome):
    try:
        lista = open(nome, 'rt')
        lista.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        lista = open(nome, 'wt+')
        lista.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado')


def visualizar(nome):
    try:
        lista = open(nome, "rt")
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in lista:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25}{dado[1]:>3}')
    finally:
        lista.close()


def cadastrar(arqu, nome, idade):
    try:
        lista = open(arqu, 'at')
    except:
        print('Houve um erro!')
    else:
        try:
            lista.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            lista.close()
