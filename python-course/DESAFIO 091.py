# 4 jogadores jogam um dado e com resultados aleatorios, em um dicionario
# depois organiza o dicionario e o jogador com maior numero ganha.

from random import randint

jogadores = {}
# Preenchendo Dicionario
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)

# Ordenando Dicionario
aux = sorted(jogadores.values())
for i in range(0, 4):
    jogadores[f'jogador{i+1}'] = aux[i]

# Mostranos Dicionario
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')

jogadores = dict(reversed(jogadores.items()))
print('Ranking dos jogadores:')

r = 0
for k, v in jogadores.items():
    r += 1
    print(f'    {r}º lugar: {k} com {v}')
