# Programa que le varios numeros  e mostra a media deles, qual maior e qual menor.

resposta = 'S'
b = maior = menor = media = n = 0

while resposta[0] != 'N':
    b += 1
    n = int(input(f'Digite o {b}º valor:'))
    resposta = str(input('Quer continuar [S/N]:')).upper().strip()
    media += n
    if menor == 0 or n < menor:
        menor = n
    else:
        if n > maior:
            maior = n
media = media / b
print(f'A media dos valores é {media:.2f}\nMaior valor digitado {maior}\n'
      f'Menor valor digitado {menor}')

