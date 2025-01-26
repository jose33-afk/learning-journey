# programa que le varios numeros e so para quando digitado 999
# mostra a soma e quantos numeros foram digitados.

print('DIGITE 999 PARA PARAR\n---------------------')
n = soma = quantidade = 0

while n != 999:
    n = int(input('Digite um valor:'))
    if n != 999:
        quantidade += 1
        soma += n
print(f'Soma de todos os valores({soma})')
print(f'Total de numeros digitados [{quantidade}]')

