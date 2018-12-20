import socket
import time
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)
dest = (socket.gethostname(), 8888)

try:
    msg = ' '
    for i in range(5):
        # Envia mensagem vazia apenas para indicar a requisição
        s.sendto(msg.encode('utf-8'), dest)
        retorno, cliente = s.recvfrom(1024)
        #print(retorno)
        lista = pickle.loads(retorno)
        time.sleep(1)
        print(lista)

    #s.send(msg.encode('ascii'))
except socket.timeout:
    s.sendto(msg.encode('utf-8'), dest)

s.close()