# Programa que escreve o numero escolhido entre zero e 20.

escolha = 0
resp = 'S'
while resp[0] not in 'N':
    while True:
        escolha = int(input('Digite um numero de 0 a 20:'))
        if 0 <= escolha <= 20:
            break
    nomes = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',
             'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
             'Quinze', 'Dezeseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    print(f'voce digitou o numero {nomes[escolha]}')
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()
        if resp.isalpha() and resp[0] in 'SN':
            break
print('Fim do programa.')
