# Escreva um programa cliente e servidor sobre TCP em Python em que:
# O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
# O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao
# cliente de volta.


import socket
import pickle
# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((socket.gethostname(), 8881))
    msg = ' '
    print(msg)
    for i in range(10):
        s.send(msg.encode('ascii'))
        bytes = s.recv(1024)
        lista = pickle.loads(bytes)
        print(lista)
        msg = 'fim'
    s.send(msg.encode('ascii'))
except Exception as erro:
    print(str(erro))

s.close()

input("Pressione qualquer tecla para sair...")