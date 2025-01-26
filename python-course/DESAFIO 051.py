# razao de e progressao aritimetica

print('Progresso aritimetica de 10 termos.')
a1 = int(input('Primeiro termo:'))
raz = int(input('Razao:'))
print(f'{a1} -> ', end='')

for c in range(1, 10):
    a1 += raz
    print(f'{a1} -> ', end='')
print('End.')
