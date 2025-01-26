# matriz up, soma de todos os valores pares, soma dos valores da terceira coluna
# E o maior valor da segunda coluna.

matriz = [[], [], []]
# preenchendo
for li in range(0, 3):  # linha
    for c in range(0, 3):  # coluna
        matriz[li].append(int(input(f'Digite um valor para [{li}, {c}]: ')))

# monstrar / condiçoes
print('-=-'*15)
somap = soma3coluna = maiorvalor2li = 0
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[li][c]:^5} ]', end='')
        if matriz[li][c] % 2 == 0:
            somap += matriz[li][c]
        if li == 1:
            if matriz[1][c] > maiorvalor2li:
                maiorvalor2li = matriz[1][c]
    soma3coluna += matriz[li][2]
    print()

print('-=-'*15)
print(f'A soma dos valores pares é {somap}.')
print(f'A soma dos valores da Terceira coluna é {soma3coluna}.')
print(f'O maior valor da segunda linha é {maiorvalor2li}')
