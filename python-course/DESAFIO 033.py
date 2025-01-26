# Programa que lê três números e mostra qual é maior e qual é menor

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numeoro:'))
n3 = int(input('Digite o terceiro numero:'))

if n1 > n2 and n1 > n3:  # Maior
    print(f'Maior numero digitado, {n1}')
if n2 > n1 and n2 > n3:
    print(f'Maior numero digitado, {n2}')
if n3 > n1 and n3 > n2:
    print(f'Maior numero digitado, {n3}')

if n1 < n2 and n1 < n3:  # Menor
    print(f'Menor numero digitado, {n1}')
if n2 < n1 and n2 < n3:
    print(f'Menor numero digitado, {n2}')
if n3 < n1 and n3 < n2:
    print(f'Menor numero digtado, {n3}')

