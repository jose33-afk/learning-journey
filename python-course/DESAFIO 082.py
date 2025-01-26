# Programa que lê varios numeros e cria três listas uma com todos os numeros
# uma com os numeros pares e uma com numeros Impares

listan = []
listai = []
listap = []
while True:
    nume = int(input('Digite um número: '))
    listan.append(nume)
    if nume % 2 == 0:
        listap.append(nume)
    else:
        listai.append(nume)
    parar = str(input('Quer continuar [S/N]? '))
    if parar in "Nn":
        break
print('-=-'*15)
print(f'A lista completa é {listan}')
print(f'A lista de Pares é {listap}')
print(f'A lista de Impares é {listai}')
