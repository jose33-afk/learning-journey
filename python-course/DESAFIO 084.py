# Nome e peso de varias pessoass e poe uma lista
# com as pessoas mais pesadas, e menos pesadas.

pessoas = []
dados = []
maior = []
menor = []
totalpess = maiorpeso = menorpeso = 0
while True:
    totalpess += 1
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    
    # Menor e Maior peso
    if totalpess == 1:
        maiorpeso = menorpeso = dados[1]
    elif dados[1] > maiorpeso:
        maiorpeso = dados[1]
    elif dados[1] < menorpeso:
        menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    # Parar
    parar = ' '
    while parar not in 'NnSs':
        parar = input('Quer continuar? [S/N]')
    if parar in 'Nn':
        break

# nomes pessoas pesadas
for p in pessoas:
    if p[1] == maiorpeso:
        maior.append(p[0])
    elif p[1] == menorpeso:
        menor.append(p[0])

print('-=-'*15)
print(f'Ao todo, você cadrastrou {totalpess} pessoas.')
print(f'O Maior peso foi de {maiorpeso}Kg. Peso de {maior}')
print(f'O menor peso foi de {menorpeso}Kg. Peso de {menor}')
