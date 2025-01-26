# Lê nome, sexo, idade de varias pessoas, guardos em uma lista
# A quantas pessoas foram quadratadas B A media de idade do grupo
# C Uma lista com todas as mulheres D Uma lista com todas as pessoas acima da media

from copy import copy

pessoas = list()
soma = 0
mulher = []
pessoa = dict()

while True:
    # Preenchendo dicionario
    pessoa['nome'] = str(input('\033[1;97mNome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('\033[1;31mERRO! por favor, digite apenas M ou F.\033[1;97m')
    pessoa['idade'] = int(input('Idade: '))

    # Mulheres
    if pessoa['sexo'] in 'F':
        mulher.append(copy(pessoa['nome']))

    # Soma idade/ Preenchendo lista
    soma += pessoa['idade']
    pessoas.append(copy(pessoa))

    # Parar
    while True:
        parar = str(input('Quer continuar [S/N]? ')).upper()
        if parar in 'SN':
            break
        print('\033[1;31mERRO! apenas S ou N.\033[1;97m')
    if parar == 'N':
        break

print('-=-'*15)
print(f' - Ao todo temos {len(pessoas)} pessoas Cadastradas.')
print(f' - A média de idade é {soma / len(pessoas):.2f} anos.')
print(' - As mulheres cadastradas Foram: ', end='')
if len(mulher) > 0:
    for m in mulher:
        print(m, end=' ')

# pessoas acima da media de idade
for p in pessoas:
    print()
    if p['idade'] > soma / len(pessoas):
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
print()
print(f'{"<< ENCERRADO >>":^40}')
