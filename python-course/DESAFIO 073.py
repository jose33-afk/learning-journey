# Programa opçoes de manipulaçao de Tabela do brazileirao

tabelatime = ('Flamento', 'Bahia', 'Botafogo', 'Athletico-PR', 'Sao Paulo', 'Palmeiras', 'Cruzero',
              'Atletico-MG', 'Bragantino', 'Internacional', 'Fortaleza', 'Juventude', 'Gremio',
              'Vasco', 'Corinthias', 'Fluminence', 'Criciuma', 'Atletico-GO', 'Cuiaba', 'Vitoria')
# Cores
co = {'n': '\033[m', 'b': '\033[1;97m', 'v': '\033[1;31m', 'a': '\033[1;33m'}

while True:
    print(f'{co['b']}==============================\n'
          'Tabela de times\n'
          '------------------------------\n'
          '[1] para mostrar a tabela completa\n'
          '[2] para mostrar o top 5\n'
          '[3] ultimos 4 colocados\n'
          f'[4] Tabela em ordem alfabetica\n'
          '[5] Sair\n'
          f'==============================')
    # Erro caso algo diferente de 1 a 5
    resp = '0'
    while resp[0] not in '12345':
        resp = input(f'->')
        if resp not in '12345':
            print(f'{co['v']}Erro tente novamente.{co['n']} ')
        if len(resp) == 0:
            resp = 'T'

    # Tabela completa
    if resp == '1':
        print('Tabela completa')
        print('-'*30)
        pos = 0
        for c in range(0, 20):
            pos += 1
            if c > 15:
                print(f'{co['v']}Posiçao {pos}º{co['b']} {tabelatime[c]}')
            else:
                print(f'Posiçao {pos}º {tabelatime[c]}')
        print('-' * 30)

    # Primeiros 5 colocados
    if resp == '2':
        print(f'Top 5{co['a']}')
        pos = 0
        for c in range(0, 5):
            pos += 1
            print(f'Posiçao {pos}º {tabelatime[c]}')

    # Ultimos 4 colocados
    if resp == '3':
        print('Ultimos 4 colocados')
        pos = 16
        for c in range(16, 20):
            pos += 1
            print(f'{co['v']}Posiçao {pos}º {tabelatime[c]}')

    # tabela em ordem
    if resp == '4':
        print('\033[1;34m', sorted(tabelatime))
    if resp == '5':
        break
print('\033[1;32mPrograma Finalizado')
