# Programa que lê um nome de uma cidade e diz se ela começa com 'SANTO'

nome = str(input('Digite um nome: ')).strip()
n = nome.split()
print(f'O {nome} comceça com "SANTO?" {'SANTO' in n[0].upper()}')
