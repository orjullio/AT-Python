import time
import random

def fatorial(x):
    result = 1
    for i in range(x):
        fator_i = (x-i)
        result = result*fator_i
    return result

N = int(input("Entre com o tamanho do vetor: "))
t_inicio = float(time.time())

vetorA = []
for i in range(N):
    vetorA.append(random.randint(0,N))
print(vetorA)

vetorB = []
for i in vetorA:
    vetorB.append(fatorial(i))

t_fim = float(time.time())
print("Fatorial:", vetorB)
print("Tempo total:", t_fim - t_inicio)