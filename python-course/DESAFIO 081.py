# lê varios valores e poe em uma lista, mostra em ordem decrescente,
# quantos valores foram digitados e se o 5 esta na lista

valors = []
cont = valor = 0
while True:
    parar = 'e'
    valors.append(int(input('Digite um valor: ')))
    cont += 1
    while parar not in 'SN':
        parar = str(input('Quer continuar [S/N]')).upper()
    if parar == 'N':
        break

valors.sort(reverse=True)
print('-=-'*15)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {valors}')
if 5 in valors:
    print('O valor 5 Faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
