import socket
import pickle
import os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 8881
socket_servidor.bind((host, porta))

socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    msg = socket_cliente.recv(1024)
    if msg.decode('ascii') == 'fim':
        break
    resposta = []
    lista_arq = os.listdir('.')
    for i in lista_arq:
        resposta.append(i)
    bytes_resp = pickle.dumps(resposta)
    socket_cliente.send(bytes_resp)
socket_cliente.close()
socket_servidor.close()