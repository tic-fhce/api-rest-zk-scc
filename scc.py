#CLASE DATOS DE CONECCION
path = 'base/conection.txt'
URL = ''
IP = ''
PORT = 0
TIMEOUT = 5
PASSWORD = 0
FORCEUDP = False
OMMITPING = False
LUGAR = ''
dato = ''

with open(path) as archivo:
    for linea in archivo:
        dato = linea.replace("\n", "")
        if(dato.__contains__('URL')):
            URL = dato.replace('URL', '')
        if(dato.__contains__('ip')):
            IP = dato.replace('ip', '')
        if (dato.__contains__('prt')):
            PORT = int(dato.replace('prt', ''))
        if (dato.__contains__('bol')):
            FORCEUDP = eval(dato.replace('bol', ''))
        if (dato.__contains__('Lugar')):
            LUGAR = dato.replace('Lugar', '')