import os
import psutil

print(psutil.disk_partitions())

#print(sdiskusade)

#teste = 'C:\Users\Rodrigo\PycharmProjects\DPRT-AT\Cachorro'

#print('Uso do disco: {}'.format(psutil.disk_usage(path='C:')))


# print(psutil.disk_io_counters())

#print('Tamanho arquivo: {}'.format(os.path.getsize('Cachorro')))

pasta = str(input('Digite o nome de uma pasta\n'))

os.mkdir(pasta)

lista_diretorio = os.listdir('.')
for i in lista_diretorio:
    nome_arquivo = os.path.abspath(i)
    print(nome_arquivo)


dir_path = 'C:/Users/Rodrigo/PycharmProjects/DPR-AT/{}/'.format(str(pasta))
files = os.listdir(dir_path)
for f in files:
    f_path = os.path.join(dir_path,f)
    f_size = os.path.getsize(f_path)
    f_size_kb = f_size/1024 # obter resultado em kB
    print(f_path, f_size_kb)






