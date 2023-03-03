cidade = input('Digita o nome da sua cidade: ').strip()
divide = cidade.upper().split()
tem = 'SANTO' in divide[0]
print('O nome da sua cidade começa com "Santo"? ', tem)