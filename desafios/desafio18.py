import math
ang = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno de {}° é {:.4f}'.format(ang,sen))
print('O cosseno de {}° é {:.4f}'.format(ang,cos))
print('A tangente de {}° é {:.4f}'.format(ang, tan))


