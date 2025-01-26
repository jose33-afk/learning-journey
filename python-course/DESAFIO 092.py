# Mostra idade, Com quantos anos será sua aposentadoria, e outros detalhes do trabalhador

from datetime import datetime
from copy import copy

# Recolhendo Informaçoes
contribuente = dict()
contribuente['nome'] = str(input('Nome: '))
ida = int(input('Ano de nascimento: '))
date = datetime.now().year
contribuente['idade'] = date - ida  # Calculo idade
contribuente['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

# Nao tem Carteira de trabalho
if contribuente['ctps'] == 0:
    print('-=-' * 15)
    for k, v in contribuente.items():
        print(f' - {k.capitalize()} tem o valor {v}')
else:
    # Tem carteira
    contribuente['contratacao'] = int(input('Ano de contraçao:'))
    contribuente['salario'] = float(input('Salário: R$'))
    anosfalta = 35 - (date - contribuente['contratacao'])
    idade = copy(contribuente['idade'])
    contribuente['aposentadoria'] = idade + anosfalta
    print('-=-' * 15)
    for k, v in contribuente.items():
        print(f' - {k.capitalize()} tem o valor {v}')
