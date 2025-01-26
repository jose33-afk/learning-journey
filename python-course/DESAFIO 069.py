# le idade e o sexo de varias pessoas, Mostra quantas pessoas tem mais de 18 anos,
# quantos homens foram cadrastrados quantas mulheres tem menos de 20 anos.

quantimais18 = quantihoms = quantimulhe20 = 0
idade = ''
b = '\033[1;97m'
nd = '\033[m'
vm = '\033[1;31m'
az = '\033[1;34m'
rx = '\033[1;35m'
vd = '\033[1;32m'

while True:
    print(f'{b}-' * 29)
    print('     CADASTRE UMA PESSOA        ')
    print('-' * 29)

    # Le numero e teste se é numero
    idade = ''
    while not idade.isnumeric():
        idade = str(input(f'{b}Idade:{nd}'))
        if not idade.isnumeric():
            print('\033[1;31mErro somente numeros!')
    idade = int(idade)

    # Le [M/F] e teste se é M ou F
    while True:
        sexo = str(input(f'{b}Sexo [{az}M{b}/{rx}F{b}]:{nd}')).upper().strip()
        if sexo.isalpha():
            if sexo in 'FM':
                break
            else:
                print(f'{vm}Somente! {rx}F{b} or {az}M{nd}')
        else:
            print(f'{vm}Somente {rx}F{b} or {az}M{nd}')

    # Funçao do programa.
    if idade > 18:
        quantimais18 += 1
    if sexo == 'M':
        quantihoms += 1
    else:
        if idade < 20 and sexo == 'F':
            quantimulhe20 += 1

    # Le e testa se digitou S ou N.
    parar = str(input(f'{b}Quer continuar? [{vd}S{b}/{vm}N{b}]:{nd}')).upper().strip()
    while 'S' != parar != 'N':
        print(f'{vm}Erro')
        parar = str(input(f'{b}Somente! [{vd}S{b}/{vm}N{b}]:{nd}')).upper().strip()
    if parar == 'N':
        break
print(f'{vd}=====Progama Finalizado!======{b}')
print(f'Total de pessoas com mais de 18 anos:{quantimais18}')
print(f'Temos {quantihoms} Homens cadastrados!')
print(f'E temos {quantimulhe20} com menos de 20 anos.')
