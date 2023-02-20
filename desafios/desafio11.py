largura = float(input('Insira a largura do local em metros: '))
altura = float(input('Insira a altura do local em metros: '))
area = largura * altura
tinta = area/2
print('Com 1L de tinta é possível pintar 2 m².  De acordo com área do seu local, {}m², é preciso {}L de tinta.'.format(area, tinta))
