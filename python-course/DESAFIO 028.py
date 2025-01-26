# Programa faz o computador 'pensar' em um numero inteiro entre 0 e 5,
# e peça para o usuario tentar descobrir qual o numero escolhido pelo computador.

import random
print('Pensando...')
es = int(input('Adivinhe o numero entre 0 e 5 q eu escolhi!\nQual numero eu escolhi? '))
ns = random.randint(0, 5)
if es == ns:
    print(f'Nossa vc acertou eu escolhi o numero {ns}')
else:
    print(f'Voce errou eu escolhi o numero {ns}')
