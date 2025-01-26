# Programa que mostra a tabuada do numero selecionado
# Para quando o numero for negativo

tab = cont = 0

while True:
    tab = int(input('Digite a tabuada desejada:'))
    if tab == 0:
        tab = int(input('\033[1;30;41mN existe tabuada do 0 digite novamente!\033[m .'))
    if tab <= 0:
        break
    print('\033[1;97m-' * 20)
    while cont != 10:
        cont += 1
        print(f'{tab} x {cont} = {tab * cont}')
    print('\033[1;97m-' * 20)
    cont = 0
print('\033[1;30;42mTabuadas Finalizadas!\033[m')
