# Escreva um programa em Python que:
# obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu
# programa manipula suas informações;

import psutil, time

lista = psutil.pids()
processo = psutil.Process()

for i in range(len(lista)):
    time.sleep(1)
    identi = lista[i]
    nome = psutil.Process(identi)
    cpu = processo.cpu_percent()
    print('Id: {}   Nome: {}    Porcentagem da CPU: {}'.format(identi, nome, cpu))








