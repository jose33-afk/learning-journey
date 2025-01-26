# Programa que lê dois numeros interios e somare-os,
# O primeiro valor é maior, O segundo é maior, n exieste valor maior, os valores sao iguais.

n = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
if n > n2:
    print(f'\033[1;33mMaior valor é \033[1;32m{n}\033[1;33m e o menor é \033[1;31m{n2}!')
elif n == n2:
    print('\033[31mNao existe maior valor ou menor pq os dois sao iguais!')
else:
    print(f'\033[1;33mMaior valor é \033[1;32m{n2}\033[1;33m e o menor é \033[1;31m{n}!')

