# Programa que lê um numero inteiro e mostra se é impar ou par

num = int(input('Digite um numero:'))
print('-=-'*10)
if num % 2 == 0:
    print(f'O valor {num} é PAR!')
else:
    print(f'O valor {num} é IMPAR!')
print('-=-'*10)
