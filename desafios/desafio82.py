lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? (S/N) ')).upper()
    if resp[0] == 'N':
        break
for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(lista)
print(par)
print(impar)
