# Programa que simula um caixa eletronico.

print('='*30)
print('           BANCO B')
print('='*30)
valor = int(input('Que valor voce quer sacar? R$'))
resto = cont = total5 = 0

# Cedulas de #50
divi50 = valor // 50
if divi50 != 0:
    print(f'Total de {divi50} cedulas de R$50')
    a = divi50 * 50
    for c in range(a, valor):
        resto += 1
else:
    resto = valor

# Cedulas de R$20
divi20 = resto // 20
if divi20 != 0:
    print(f'Total de {divi20} cedulas de R$20')
    while cont < divi20:
        resto -= 20
        cont += 1

# Cedulas de R$10
divi10 = resto // 10
if divi10 != 0:
    cont = 0
    print(f'Total de {divi10} cedulas de R$10')
    while cont < divi10:
        resto -= 10
        cont += 1

# Cedulas de R$1
divi5 = resto // 1
if divi5 != 0:
    for cont in range(1, divi5+1):
        total5 += 1
    print(f'Total de {total5} cedulas de R$1')
print('='*30)
