# programa que leia quatro valores pelo teclado e guardeos em um tupla
# No final mostra A quantas vezes o 9 apareceu B em que posicao o primeiro 3
# foi emcontrado e quais foram os numeros pares.

n = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')),
     int(input('Digite mais um numero: ')), int(input('Digiteo ultimo numero: ')))
v = len(n) - 1
contp = busc3 = np = 0
junt = ()
print(f'Voce digitou os valores {n}')

for c in range(0, len(n)):
    if n[c] == 3:
        busc3 += 1

print(f'O valor 9 apareceu {n.count(9)} vezes')
if busc3 >= 1:
    print(f'O valor 3 apareceu na posiçao {n.index(3) + 1}º')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print(f'Os valores pares digitados foram ', end='')
for c in range(0, len(n)):
    if n[c] % 2 == 0:
        print(f'{n[c]} ', end='')
