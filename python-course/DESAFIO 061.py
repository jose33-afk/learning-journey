# Programa refeito com for

print('Progressao aritimetica 2.0v')
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razao:'))
print(primeiro, end=' ->')
c = pro = 0

while c < 9:
    primeiro += razao
    print(f' {primeiro} -> ', end='')
    c += 1
print('Fim')
