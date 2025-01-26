# Lê sete valores, recebe valores pares e impares em duas listas separadas.

pares = list()
impares = list()
numeros = [pares, impares]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º Valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 > 0:
        impares.append(valor)

pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
