# Programa que le nome duas notas de varios alunos e guarda em uma kista composta.
from time import sleep
nomes = []
pessoas = []
notas = []

# Preenchendo.
while True:
    nomes.append(str(input('\033[1;97mNome: ')))
    notas.append(float(input('Primeira Nota: ')))
    notas.append(float(input('Segunda nota: ')))
    nomes.append(notas[:])
    nomes.append((notas[0] + notas[1]) / 2)
    notas.clear()
    pessoas.append(nomes[:])
    nomes.clear()
    parar = ' '
    while parar not in 'NnSs':
        parar = str(input('Quer continuar? [S/N] '))
    if parar in 'Nn':
        break

# Monstrando Tabela.
print('-=-'*25)
print(f'No. Nome {"MÉDIA":>10}')
print('---'*10)
for a in range(0, len(pessoas)):
    print(f'{a}   {pessoas[a][0]:15}{pessoas[a][2]}')

# Mostrar notas
print('---'*15)
qual = 0
while qual != 999:
    qual = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if qual != 999:
        if qual <= len(pessoas) - 1:
            print(f'\033[1;32mNotas de {pessoas[qual][0]} são {pessoas[qual][1]}\033[1;97m')
        else:
            print('\033[1;31mErro!\033[1m Aluno não exite Tente novamente.\033[1;97m')
print('FINALIZANDO....')
sleep(1.0)
print('<<< VOLTE SEMPRE >>>')
