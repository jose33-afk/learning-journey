# Programa pra ler o peso de 5 pessoas e no final mostrar qual foi o maior pesso e o menor peso lido.

pmaior = 0
pmenor = 0

for c in range(1, 6):
    peso = float(input(f'\033[1;37mDigite o peso(Kg) da {c}ª pessoa: '))
    if peso > pmaior:
        pmaior = peso
    if pmenor == 0 or peso < pmenor:
        pmenor = peso

print(f'\033[1;36mA pessoa com maior peso tem {pmaior}Kg\n'
      f'E a com Menor peso tem {pmenor}Kg')
