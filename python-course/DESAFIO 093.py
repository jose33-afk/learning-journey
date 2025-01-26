# Gerencia o aproveitamento de um jogador futebol lê nome do jogador,
# quantas partidas, quantidade de gols, total de gols.

dados = dict()
gols = list()

dados['nome'] = str(input('\033[1;97mNome do jogador: '))
quantpart = int(input(f'Quantas partidas {dados['nome']} Jogou? '))

# Gols partida
for c in range(0, quantpart):
    gols.append(int(input(f'   Quantos gols na partida {c}? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)

# Monstrando dados do Dicionario
print('-=-'*15)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*15)

# Relatorio das partidas.
print(f'O jogador {dados['nome']} jogou {quantpart} partidas.')
for pos, va in enumerate(gols):
    print(f'   => Na partida {pos}, fez {va} gols.')
print(f'Foi um total de {dados['total']} Gols!')
