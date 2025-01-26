# Upgrade do desafio 93, Para que ele funcione para varios jogadores, incluindo um sistema de
# visualizaçao de detalhamento do aproveitamento de cada jogador.

dados = dict()
gols = list()
jogadores = list()

while True:
    print('\033[1;97m==='*15)
    dados['nome'] = str(input('Nome do jogador: '))
    quantpart = int(input(f'Quantas partidas {dados['nome']} Jogou? '))

    # Gols partida
    for c in range(0, quantpart):
        gols.append(int(input(f'   Quantos gols na partida {c+1}? ')))

    # Guardando dados
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    gols.clear()

    # Parar
    while True:
        parar = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if parar in 'NS':
            break
        print('\033[1;31mERRO! Digite apenas S ou N!\033[1;97m')
    if parar in 'N':
        break

# Tabela Seleçao
print('-=-'*15)
print(f'Cod {"Nome":15}{"Gols":15}Total')
print('---'*15)
for pos, itms in enumerate(jogadores):
    print(f"  {pos} {itms['nome'].capitalize():15}{str(itms['gols']):20}{itms['total']}")
print('---'*15)

# Mostrando dados selecionado
ranglist = list(range(0, len(jogadores)))  # Numeraçao de jogadores
while True:
    # Verificando qualj
    while True:
        qualj = int(input('Mostrar dados de qual jogador? (999 para parar): '))
        if qualj in ranglist or qualj == 999:
            print('---' * 15)
            break
        print(f'\033[1;31mERRO! Não existe Jogador'
              f'com código {qualj}! Tente novamente\033[1;97m')
    if qualj == 999:
        print('\033[1;32m<< VOLTE SEMPRE >>')
        break

    # Tabela gols.
    print(f'--- LEVANTAMENTO DO JOGADOR \033[1;33m{jogadores[qualj]['nome'].upper()}:\033[1;97m')
    for pos, g in enumerate(jogadores[qualj]['gols']):
        if g == 0:
            print(f'\033[1;31m    No jogo {pos+1} fez {g} gols.\033[1;97m')
        else:
            print(f'\033[1;32m    No jogo {pos+1} fez {g} gols.\033[1;97m')
    print('---' * 15)
