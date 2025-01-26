"""for c in range(1, 10:
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

n = 0
while n != 1:
    n = int(input('Digite um numero:'))
print('Fim')

r = 'S'
while r == 'S':
    r = str(input('Quer continuar [S/N]:')).upper()
print('Fim')

par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} Numeros impares!')"""

'''
escolha = ''
while True:
    escolha = str(input('Digite um numero de 0 a 20:'))
    if escolha.isnumeric() and escolha <= '20':
        break
escolha = int(escolha)
nomes = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',
         'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
         'Quinze', 'Dezeseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print(f'voce digitou o numero {nomes[escolha]}')'''

valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')