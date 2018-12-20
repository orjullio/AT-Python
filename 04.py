# Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso.

arquivo = open('palavras.txt', 'r')


for i in arquivo:
    print(i[::-1])
arquivo.close()


