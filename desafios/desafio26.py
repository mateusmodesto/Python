frase = input('Digita uma frase: ').strip().lower()
print('Apareceu {} vezes a letra "A" na sua frase'.format(frase.count('a')))
print('Apareceu pela primeira vez no caracter: {}'.format(frase.find('a')+1))
print('Apareceu pela última vez no caracter: {}'.format(frase.rfind('a')+1))