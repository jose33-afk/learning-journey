# Programa refeito exercicio 61

print('Progressao aritimetica 3.0v')
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razao:'))
print(primeiro, end=' ->')

c = mais = quantidadet = 0
quer = ''
termos = 9
cguarda = 8

while c < termos:
    primeiro += razao
    print(f' {primeiro} -> ', end='')
    if c == cguarda:
        quer = str(input('Pausa.. Quer mais termos? [S/N]:')).upper()
        if quer[0] == 'S':
            mais = int(input('Quer mais quantos? '))
            termos += mais
            cguarda = termos - 1
    c += 1
    quantidadet += 1
print('Fim')
print(f'O programa foi finalizado com um total de {quantidadet + 1} Termos.')

