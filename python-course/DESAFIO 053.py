# Ler uma frase e diz se É ou Nao é um palindromo.

frase = str(input('\033[1;36mQual frase gostaria de verificar se é um palindromo? ')).strip().lower()
print('\033[1;97m-\033[1;36m'*80)
print(f'A frase [{frase.capitalize()}] invertida fica (', end='')  # continua
frase = frase.split()

comprimento = len(frase)  # comprimento da frase dividida em palavras.
frase_espacos = ''
comprimentofrase = 0
frase_invertida = ''

for cont in range(0, comprimento):  # tira os espaços.
    frase_espacos += frase[cont]

comprimentofrase = len(frase_espacos)  # comprimento sem espaços.

for c in range(comprimentofrase - 1, -1, -1):  # Inverte a frase(sem espaços).
    frase_invertida += frase_espacos[c]

print(f'{frase_invertida.capitalize()}).')  # Aqui
print('\033[1;97m-'*80)

if frase_espacos == frase_invertida:  # Verifica se é ou nao é um palindromo.
    print('\033[1;30;42mEla é um palindromo pos podemos ler das duas direçoes!')
else:
    print('\033[1;30;41mA frase n é um palindomo pos n podemos ler das duas direçoes.')
