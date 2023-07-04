import uteis
import arquivo
from time import sleep

arqu = 'cadastradas.txt'

if not arquivo.arquExiste(arqu):
    arquivo.criarArquivo(arqu)


while True:
    uteis.titulo('MENU PRINCIPAL')
    resp = uteis.menu(['Ver Pessoas Cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resp == 1:
        uteis.titulo('PESSOAS CADASTRADAS')
        arquivo.visualizar(arqu)
    elif resp == 2:
        uteis.titulo('CADASTRAR')
        nome = str(input('Nome: '))
        idade = uteis.leiaInt('Idade: ')
        arquivo.cadastrar(arqu, nome, idade)
    elif resp == 3:
        uteis.titulo('Saindo... Até Logo!')
        break
    else:
        print('\033[0;31m Digite uma opção válida! \033[m')
    sleep(2)
