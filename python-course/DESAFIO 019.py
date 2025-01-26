# Programa que sorteia um aluno de quatro alunos

from random import choice
nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
print(f'O aluno escolhido foi {choice(lista)}')
