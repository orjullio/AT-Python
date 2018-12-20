# Escreva um programa em Python que:
# gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles
# ocupam em disco. Obtenha o nome do diretório do usuário.
# Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort
# ou sorted);
# gere um arquivo texto com os valores desta estrutura ordenados.
import os

print('Exerciio 3\n')
usuario = str(input('Olá, por favor digite seu nome:\n'))
print('Obrigado {}'.format(usuario))
diretorio = str(input('Agora por favor, digite um nome para o diretório:\n'))

try:
    os.mkdir(diretorio)
except FileExistsError:
    print('Já existe um diretório com esse nome: ')
except Exception as e:
    print(str(e))

dir_path = 'C:/Users/Rodrigo/PycharmProjects/DPR-AT/{}/'.format(str(diretorio))
files = os.listdir(dir_path)
for f in files:
    f_path = os.path.join(dir_path,f)
    f_size = os.path.getsize(f_path)
    f_size_kb = f_size/1024 # obter resultado em kB
    print(f_path, f_size_kb)



