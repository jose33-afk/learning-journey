# Mini sistema, que ultilisa interactive help, O usuario vai digitar
# o comando  e o manual vai mostrar as infomaçoes dele, para quando digitado fim

from time import sleep


def manual(func):
    esc = f"Acessando o manual do comando '{func}'"
    cpr = len(esc) + 2          # comprimento do esc com a sting func
    print('\033[1;34m-' * cpr)  # linha formatada com tamanho da esc + 2 de espaço
    print(f'{esc:^{cpr}}')      # Escreve esc centralizada no tamanho do comprimento do esc
    print('-' * cpr, '\033[1;97m')
    sleep(0.5)
    help(func)


while True:
    print('\033[1;33m~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  SISTEMA DE AJUDA PYhelp')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;97m')
    f = str(input('Funçao ou Biblioteca (FIM) para parar > ')).lower()
    if f in 'fim':
        print('\033[1;31m~~~~~~~~~~~~')
        print('  ATÉ LOGO! ')
        print('~~~~~~~~~~~~')
        break
    else:
        manual(f)
