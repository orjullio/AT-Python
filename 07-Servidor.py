import socket
import pickle
import psutil

mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysocket.bind((socket.gethostname(), 8888))


while True:
    # Recebe pedido do cliente:
    msg, dest = mysocket.recvfrom(1024)
    print(msg.decode('utf-8'))

    # Gera a lista de resposta
    resposta = []
    mem = psutil.virtual_memory()
    mem_disp = mem.total - mem.used
    resposta.append(mem.total)
    resposta.append(mem_disp)
    # Prepara a lista para o envio
    bytes_resp = pickle.dumps(resposta)
    # Envia os dados
    mysocket.sendto(bytes_resp, dest)

mysocket.close()
