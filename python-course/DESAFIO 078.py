# Programa que le 5 valores e guada em uma lista, diz a posicao e o valor maior e menor

valores = list()
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao ({p}):')))
print('-=-'*15)
print(f'Voce digitou os valores {valores}')

# Maior
maior = max(valores)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c in range(0, 5):
    if valores[c] == maior:
        print(f'{c}.. ', end='')
# Menor
print()
menor = min(valores)
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for c in range(0, 5):
    if valores[c] == menor:
        print(f'{c}.. ', end='')
