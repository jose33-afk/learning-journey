# programa que le nome, idade e sexo, mostra.
# a media de idade das 4 pessoas do grupo
# qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.

from time import sleep

nome = '0'
idade = 0
sexo = '0'
mediaid = 0
maiorh = 0
nomeh = 0
qmulher = 0

for c in range(1, 5):
    nome = str(input(f'\033[1;36mDigite o nome da {c}ª pessoa:'))
    idade = int(input(f'Digite a idade da {c}ª pessoa:'))
    sexo = str(input(f'Digite o sexo da {c}ª (M/F) pessoa:')).upper().strip()
    print('-'*35)
    mediaid += idade
    if c == 1:
        maiorh = idade
    else:
        if idade > maiorh and sexo == 'M':
            nomeh = nome
            maiorh = idade
        elif idade < 20 and sexo == 'F':
            qmulher += 1

print('\033[1;33mProcessando resultado...')
sleep(1.5)
print('-' * 35)
print(f'A media de idade entre as pessoas a cima é {mediaid / 4:.1f}')
print(f'O homem mais velho é {nomeh} com {maiorh} anos de idade!')
print(f'No total existem  {qmulher} mulheres com menos de 20 anos!')
