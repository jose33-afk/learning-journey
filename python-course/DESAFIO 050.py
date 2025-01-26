# Programa lê seis numeros inteiros e mostra apenas aqueles que forem pares
# Se o valor digitado for impar ele desconside-o.

sm = 0
cp = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}. numero:'))
    if num % 2 == 0:
        sm = sm + num
        cp += 1

print(f'A soma de todos os {cp} pares é ,{sm}')


