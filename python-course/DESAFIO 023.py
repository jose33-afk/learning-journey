# Programa que lê um numero de 0 a 999 e mostra na tela cada um dos digitos separados

n = int(input('Digite um numero: '))
u = n * (10**0) % 10
d = n * (10**1)
c = n // 100 % 10
m = n // 1000
print(f'Unidade:{u}')
print(f'Dezena: {d//100%10}')
print(f'Centena:{c}')
print(f'milha: {m}')
