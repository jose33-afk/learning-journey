# Matriz

matriz = [[], [], []]

# preenchendo
for c1 in range(0, 3):
    for c2 in range(0, 3):
        matriz[c1].append(int(input(f'Digite um valor para posiçao [{c1}][{c2}]: ')))

# monstrando
print('-=-'*15)
for b1 in range(0, 3):
    for b2 in range(0, 3):
        print(f'[ {matriz[b1][b2]:^5} ]', end='')
    print()
