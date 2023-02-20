import random
name1 = str(input('Digite o nome do aluno 1: '))
name2 = str(input('Digite o nome do aluno 2: '))
name3 = str(input('Digite o nome do aluno 3: '))
name4 = str(input('Digite o nome do aluno 4: '))
ordem = [name1, name2, name3, name4]
random.shuffle(ordem)
print('A ordem dos alunos para a apresentação é: {}'.format(ordem))