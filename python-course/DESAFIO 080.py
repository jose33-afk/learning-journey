# Porgrama que ordena uma lista sem sorted

numeros = []
valor = 0
for c in range(0, 5):
    valor = int(input('Digite um numero: '))
    if c == 0:
        numeros.append(valor)
        print('Adicionado no final da lista...')
    if valor > numeros[-1]:
        numeros.append(valor)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if valor < numeros[pos]:
                print(f'Adiconado na posiçao {pos} da lista...')
                numeros.insert(pos, valor)
                break
            pos += 1
print('-=-'*15)
print(numeros)
