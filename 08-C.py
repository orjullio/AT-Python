import multiprocessing
import time
import random

def fatorial(x):
    result = 1
    for i in range(x):
        fatorial_i = (x-i)
        result = result*fatorial_i
    return result

if __name__ == "__main__":
    N = int(input("Entre com o tamanho do vetor: "))


    t_inicio = float(time.time())

    vetorA = []
    for i in range(N):
        vetorA.append(random.randint(0, N))
    print(vetorA)

    NProc = 4

    q_entrada = multiprocessing.Queue()

    q_saida = multiprocessing.Queue()

    lista_proc = []
    for i in range(NProc):
        ini = i * int(N/NProc)
        fim = (i + 1) * int(N/NProc)
        q_entrada.put(vetorA[i])
        p = multiprocessing.Process(target=fatorial, args=(q_entrada,
    q_saida))
        p.start()
        lista_proc.append(p)

    for p in lista_proc:
        p.join()

    vetorB = []
    for i in vetorA:
        vetorB.append(fatorial(i))


    t_fim = float(time.time())
    print("Fatorial:", vetorB)
    print("Tempo total:", t_fim - t_inicio)