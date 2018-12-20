# Escreva um programa em Python que:
# gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles
# ocupam em disco. Obtenha o nome do diretório do usuário.
# Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort
# ou sorted);
# gere um arquivo texto com os valores desta estrutura ordenados.
import os, sys

def main():
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
    arquivos = os.listdir(diretorio)
    dados = []
    for arquivo in arquivos:
        p = os.path.join(diretorio, arquivo)
        dado = os.stat(p)
        dados.append({'nome: ': arquivo, 'tamanho: ': dado.st_size})

    dados.sort(key=lambda l: l['tamanho'])
    print(dados)



if __name__ == '__main__':
    main()

