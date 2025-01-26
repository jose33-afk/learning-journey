# Programa q lê um numero Real qualquer pelo teclado
# e mostra na tela sua porçao inteira

from math import trunc
n = float(input('Digite um numero: '))
print(f'O numero digitado foi {n} e sua porçao inteira é {trunc(n)}')
