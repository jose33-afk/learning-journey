# Programa que gera 5 numeros aletorios e colaca em
# uma tupla. fala qual maior e menor valor na mesma

from random import randint

# preechendo a tupla
p1 = randint(1, 10)
p2 = randint(1, 10)
p3 = randint(1, 10)
p4 = randint(1, 10)
p5 = randint(1, 10)
numeros = p1, p2, p3, p4, p5
print('Os valores sorteados foram: ', end='')
for c in range(0, 5):
    print(numeros[c], end=" ")

# Maior
maior = menor = p1
if p2 > maior:
    maior = p2
if p3 > maior:
    maior = p3
if p4 > maior:
    maior = p4
if p5 > maior:
    maior = p5

# Menor
if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3
if p4 < menor:
    menor = p4
if p5 < menor:
    menor = p5
print('')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
