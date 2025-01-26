# Programa que sorteia a ordem de apresentaçao de quatro alunos

from random import sample
n1 = input('Digite o nome do primeiro aluno a ser sorteado: ')
n2 = input('segundo a ser sorteado: ')
n3 = input('Terceiro aluno ser sorteado: ')
n4 = input('Quarto aluno a ser sorteado: ')
lista = [n1, n2, n3, n4]
print(f'O Ordem de apresentaçao: {sample(lista, k=4)}')

