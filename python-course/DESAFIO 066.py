"""programa que le varios numeros e para quando digitado 999
   Mostra quantos numeros digitados e qual foi a soma deles."""

n = soma = numdigi = 0

while True:
    n = int(input(f'Digite um valor \033[1;97m(Stop=999)\033[m:'))
    if n == 999:
        break
    else:
        numdigi += 1
        soma += n
print(f'\033[1;32mA soma dos valores é {soma}\nao todo foram digitados {numdigi} numeros!')
