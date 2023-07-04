import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Não fooi possível acessá-lo!')
else:
    print('Tudo ok!')
