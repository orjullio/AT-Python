# Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do
# sistema Windows bloco de notas (notepad) para abrir o arquivo.
import subprocess


nome = str(input('Por favor, digite o nome que terá no arquivo texto: '))

print(subprocess.run(['notepad', '{}.txt'.format(nome)]))


