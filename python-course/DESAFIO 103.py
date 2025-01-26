# cria uma funcao ficha, com os parametros opcionais nome e gols

def ficha(n='', g='0'):
    if len(n) == 0:
        n = '<desconhecido>'
    if len(g) == 0 or g.isalpha():
        g = '0'
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


# Principal
print('--'*15)
nome = str(input('Nome do jogador: '))
gols = str(input('Números de Gols: '))
ficha(nome, gols)
