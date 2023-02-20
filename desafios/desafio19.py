import random
name1 = str(input('Digite o nome do aluno 1: '))
name2 = str(input('Digite o nome do outro aluno 2: '))
name3 = str(input('Digite o nome do outro aluno 3: '))
name4 = str(input('Digite o nome do outro aluno 4: '))
print('O aluno escolhido foi o {}'.format(random.choice([name1, name2, name3, name4])))
