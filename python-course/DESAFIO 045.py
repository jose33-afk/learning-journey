# Jogo jonkepo, computador VS usuario
from random import choice
from time import sleep

c = {'n': '\033[m', 'b': '\033[1;97m', 'r': '\033[1;35m', 'v': '\033[1;31m', 'z': '\033[1;34m',
     'am': '\033[1;33m', 'ca': '\033[1;36m', 'vv': '\033[1;30;42m', 'vv1': '\033[1;30;41m'}  # cores

esj = str(input(f'{c['b']}Escolha {c['r']}pedra{c['b']}(D){c['b']},{c['r']} papel'
                f' {c['b']}(P) ou {c['r']}tesoura{c['b']}(T):')).upper().strip()

if esj == 'D':  # Escolha do jogador
    esj = 'PEDRA'
elif esj == 'P':
    esj = 'PAPEL'
elif esj == 'T':
    esj = 'TESOURA'

ppt = ['PEDRA', 'PAPEL', 'TESOURA']  # Escolha do computador
esc = choice(ppt)
ganhador = '0'

if esc == 'PEDRA' and esj == 'TESOURA':  # Pedra/Tesoura
    ganhador = '\033[1;30;41mCOMPUTADOR GANHOU!!'
elif esc == 'TESOURA' and esj == 'PEDRA':
    ganhador = '\033[1;30;42mJOGADOR GANHOU!!!'

elif esc == 'PAPEL' and esj == 'PEDRA':  # Papel/Pedra
    ganhador = '\033[1;30;41mCOMPUTADOR GANHOU!!!'
elif esc == 'PEDRA' and esj == 'PAPEL':
    ganhador = '\033[1;30;42mJOGADOR GANHOU!!!'

elif esc == 'TESOURA' and esj == 'PAPEL':  # Tesoura/Papel/empate
    ganhador = '\033[1;30;41mCOMPUTADOR GANHOU!!!'
elif esc == 'PAPEL' and esj == 'TESOURA':
    ganhador = '\033[1;30;42mJOGADOR GANHOU!!!'
elif esc == esj:
    ganhador = '\033[1;97mEMPATE!!'

if esj == 'PEDRA' or esj == 'PAPEL' or esj == 'TESOURA':  # Jogador Escolha algo sem ser as opçoes
    print(f'{c['z']}Jo')
    sleep(0.5)
    print(f'{c['am']}ken')
    sleep(0.5)
    print(f'{c['ca']}Po')
    print(f'{c['b']}=' * 30)
    print(f'{c['b']}O computador jogou {esc}.\nO jogador jogou {esj}.{c['n']}')
    print(f'{c['b']}------------STATUS------------')
    print(f'{ganhador}{c['n']}')
    print(f'{c['b']}=' * 30)
else:
    print(f'{c['vv1']}ERRO, TENTE NOVAMENTE')
