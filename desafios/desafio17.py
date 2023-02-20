import math
from math import sqrt
cp = float(input('Digite a medida do cateto oposto: '))
cd = float(input('Digite a medida do cateto adjacente: '))
'''h = sqrt(cp**2 + cd**2)'''
h = math.hypot(cp, cd)
print('A  Hipotenusa mede {}'.format(h))