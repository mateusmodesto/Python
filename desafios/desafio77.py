lista = ('aprender', 'programar', 'estudar', 'andar', 'gratis', 'jogar', 'futuro', 'trabalhar')
for palavra in lista:
    print(f'\n Na {palavra} há as vogais: ', end='')
    for p in palavra:
        if p.lower() in 'aeiou':
            print(p, end=' ')
