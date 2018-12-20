import threading
import time
import random

def fatorial(x):
    result = 1
    for i in range(x):
        fator_i = (x-i)
        result = result*fator_i
    return result

N = int(input("Entre com o tamanho do vetor: "))# vetor so funciona até 1000

# Captura tempo inicial
t_inicio = float(time.time())

# Gera lista com valores aleatórios
vetorA = []
for i in range(N):
    vetorA.append(random.randint(0,N))
print(vetorA)

Nthreads = 4 # Número de threads a ser criado

# Vetor para salvar a soma parcial de cada thread
soma_parcial = Nthreads * [0]

lista_threads = []
for i in range(Nthreads):
    ini = i * int(N/Nthreads) # início do intervalo da lista
    fim = (i + 1) * int(N/Nthreads) # fim do intervalo da lista
    t = threading.Thread(target=fatorial, args=(vetorA[i]))
    t.start() # inicia thread
    lista_threads.append(t) # guarda a thread

for t in lista_threads:
    t.join() # Espera as threads terminarem

vetorB = []
for i in vetorA:
    vetorB.append(fatorial(i))
# Captura tempo final

t_fim = float(time.time())
# Imprime o resultado e o tempo de execução
print("Fatorial:", vetorB)
print("Tempo total:", t_fim - t_inicio)