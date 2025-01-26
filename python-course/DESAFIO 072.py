# Programa que escreve o numero escolhido entre zero e 20.

escolha = ''
while True:
    escolha = str(input('Digite um numero de 0 a 20:'))
    if escolha.isnumeric() and escolha <= '20':
        break
escolha = int(escolha)
nomes = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',
         'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
         'Quinze', 'Dezeseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print(f'voce digitou o numero {nomes[escolha]}')