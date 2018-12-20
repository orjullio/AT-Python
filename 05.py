# Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:

arquivo = open("a.txt", "r")

lista_a = []

for linha in arquivo:
    lista_a.append(linha)

lista_a.split()

arquivo.close()



print(lista_a)
