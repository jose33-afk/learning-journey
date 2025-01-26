# Mega sena, cria palpites.
from random import randint
from time import sleep

sena = []
mega = []
senateste = cont = 0
c = {'b': '\033[1;97m', 'am': '\033[1;33m'}
print(f'{c['b']}---'*12)
print(f'         JOGA NA {c['am']}MEGA{c['b']} SENA')
print('---'*12)
qunts = int(input(f'\033[34mQuantos jogos você quer que eu sorteie? '))
print(f'{c['b']}-=-=-=  SORTEANDO {qunts} JOGOS  =-=-=-')

# preenchendo
for c in range(0, qunts):
    cont = 0
    while True:
        cont += 1
        senateste = randint(1, 60)
        if senateste not in sena:
            sena.append(senateste)
        if len(sena) == 6:
            break
    sena.sort()
    mega.append(sena[:])
    sena.clear()

# mostrando
for pos, elementos in enumerate(mega):
    print(f'Jogo {pos+1} \033[1;34m{elementos}\033[1;97m')
    sleep(1)
print(f'-=-=-=-= < BOA SORTE! > =-=-=-=-')
