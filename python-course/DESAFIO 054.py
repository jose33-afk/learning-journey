# Ler a data de nascimento de 7 pessoas
# e dizer quantas ainda n atigiram a maior idade, e quantas pessoas sao de maiores.

from datetime import date

idade = 0
qmaior = 0
qmenor = 0

for c in range(1, 8):
    asc = int(input(f'\033[1;97mDigite o ano de nascimento da {c}ª pessoa:'))
    idade = date.today().year - asc
    if idade < 18:
        qmenor += 1
    elif idade >= 18:
        qmaior += 1

print('\033[1;32m-'*45)
print(f'Ao todo temos um total de \033[1;97m{qmaior}\033[1;32m velinhos.\n'
      f'E temos um total de \033[1;97m{qmenor}\033[1;32m jovens de menor!')
print('-'*45)
