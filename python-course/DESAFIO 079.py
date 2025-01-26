# Lê varios valores numericos e casdrastra-os em uma lista, ele n será adicionado
# Caso o numero ja esteja cadastrado

listnum = list()
valor = 0
while True:
    stop = 'A'
    valor = int(input('Digite um numero: '))
    if valor in listnum:
        print('\033[1;31mValor duplicado! Não vou adicionar...\033[m')
    else:
        print('\033[1;32mValor adicionado com sucesso...\033[m')
        listnum.append(valor)

    while not stop[0] in 'SN':
        stop = str(input('Quer continuar? [S/N]')).upper().strip()
        if len(stop) == 0:
            stop = 'a'
    if stop == 'N':
        break
print('-=-'*15)
listnum.sort()
print(f'Você digitou os valores {listnum}')
