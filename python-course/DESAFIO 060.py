# Fatorial De uma numero digitado.

f = int(input('Qual numero do fatorial que deseja? '))
print('-'*30)

c = f - 1
fibo = f
somaprox = 0

print(f, end='! = ')
while c > 0:
    somaprox = fibo * c
    fibo = somaprox
    print(f'x {c} ', end='')
    c -= 1

print(f'= {fibo}')
print('-'*30)
print(f'O Fatorial de {f} é {fibo}')
