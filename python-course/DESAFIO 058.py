# Computador escolhe um numero entre 0 ate 10 e o usuario tenta acertar,
# Programa so finaliza quando o usuario acertar, mostra quantos palpites foram necessarios

from random import randint
from time import sleep

print('Pensando...')
sleep(1.5)
es = int(input('Adivinhe o numero entre 0 e 10 q eu escolhi!\nQual numero eu escolhi? '))
ns = randint(0, 10)  # Escolha do pc

numerotenta = 0

if es == ns:
    print('\033[1;30;42mParabens humano voce acertou!')
else:
    while es != ns:
        if es > ns:
            print('\033[1;30;41mMenos.. Voce errou, tente novamente!\033[m')
        elif es < ns:
            print('\033[1;30;41mMais.. Voce errou, tente novamente!\033[m')
        es = int(input('Qual numero eu escolhi? '))
        numerotenta += 1

numerotenta += 1

if 2 >= numerotenta >= 1:
    print(f'\033[1;30;42mParabens voce acertou com apenas {numerotenta} tentativas!')
elif 5 >= numerotenta >= 3:
    print(f'\033[1;30;43mVoce acertou depois de {numerotenta} é Nada Mal...')
else:
    print(f'\033[1;30;41mLamentavel...')
print(f'A Escolha do computador foi {ns}.')
