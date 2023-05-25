teste = list()
teste.append('Mateus')
teste.append(15)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
print('--'*50)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[2][1])
print(galera[0])
print('-=-'*5)
for p in galera:
    print(p)
print('-=-'*5)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')
print('-=-'*15)
geral = list()
dado = list()
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    geral.append(dado[:])
    dado.clear()
print(geral)
maior = menor = 0
for d in geral:
    if d[1] >= 18:
        print(f'O {d[0]} é maior de idade')
        maior += 1
    else:
        print(f'O {d[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} pessoas de maior e {menor} pessoas de menor')
