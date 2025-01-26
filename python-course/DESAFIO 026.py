# Programa que lê uma frase pelo teclado e mostra:
# Quantas vezes a letra 'A' apareceu,
# Em que posiçao ela apareceu a primeira vez, em que posiçao ela aparece a ultima vez.

n = str(input('Digite qualquer frase:')).upper().strip()
print(f'Vezes q apareceu a letra "A":{n.count('A')}')
print(f'Posicao da primeira aparicao da letra "A" na frase: {n.find('A') + 1}')
print(f'Posicao da ultima aparicao da letra "A" na frase: {n.rfind('A') + 1}')
