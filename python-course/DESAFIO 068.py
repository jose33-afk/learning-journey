# Programa que faz o usuario jogar impar ou par com pc

from random import randint, choice

print('\033[1;33m-=-' * 7)
print('JOGUINHO PAR OU IMPAR')
print('-=-' * 7)
contidadevitoria = 0
quantidaemp = 0
while True:
    # Escolha Jogador
    numejg = input('\033[1;35mDigite o valor:').strip()

    # erro caso digite string ou espaço ou diferente de numero
    if numejg.isnumeric():
        a = False
    else:
        a = True
    if a:
        print('\033[1;31mErro tente novamente.\033[m')
        while True:
            if numejg.isspace():  # corrigindo
                print('\033[1;31mErro n digitou nada!\033[m')
            elif numejg.isalpha() or numejg.isalnum():
                print('\033[1;31mErro digitou Letra!\033[m')
            numejg = input('\033[1;97mSomente numeros!:\033[1;35m').strip()  # corrigindo
            if numejg.isnumeric():
                break

    # Erro caso digite algo diferente de impar ou par, I ou P.
    b = 0
    ipjg = str(input('Par ou Impar? [P/I]:')).upper().strip()
    if ipjg.isalpha():
        if ipjg[0] == 'P' or ipjg[0] == 'I':
            b = False
    else:
        b = True
    if b:
        while True:
            ipjg = str(input('\033[1;31mErro tente novamente. \033[1;97m[P/I]:')).upper().strip()
            if ipjg.isalpha():  # corrigindo
                if ipjg[0] == 'P' or ipjg[0] == 'I':
                    break

    # Escolha Pc
    numeropc = randint(1, 10)
    ip = ['Impar', 'Par']
    ippc = choice(ip)

    # Par ou Impar
    impoupar = ''
    n = int(numejg)
    soma = n + numeropc
    if soma % 2 == 0:
        impoupar = 'Par'
    else:
        impoupar = 'Impar'

    # mais bonitinho
    if ipjg[0] == 'I':
        ipjg = 'Impar'
    else:
        ipjg = 'Par'

    print('\033[1;97m-' * 40)
    print(f'\033[1;97mVoce jogou {numejg}\033[1;35m({ipjg})\033'
          f'[1;97m e o computador {numeropc}\033[1;34m({ippc})\033[1;97m Total {soma}\033[m.')
    print('\033[1;97m-' * 40)

    # ganhador
    if ippc != ipjg:
        if ippc == impoupar:
            print('\033[1;30;41mVoce Perdeu\033[m')
            break
        else:
            if ipjg == impoupar:
                print('\033[1;30;42mVoce GANHOU!\033[m')
                contidadevitoria += 1
    elif ippc == ipjg:
        quantidaemp += 1
        print('\033[1;30;43mVoce empatou!\033[m')
    print('\033[1;33mVamos jogar novamente...')
    print('\033[1;97m-=-\033[m' * 7)

print('\033[1;33m-=-' * 7)
print(f'\033[1;31mGAME OVER!\033[1;32m Voce venceu {contidadevitoria} vezes e \033[1;97mempatou {quantidaemp}.')
