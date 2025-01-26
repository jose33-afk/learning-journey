# Tupla unica com nome e preço de produtos, no final mostra uma lista

listaprodut = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
               4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('_'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_'*40)
prox = 1
for c in range(0, len(listaprodut), 2):
    print(f'{listaprodut[c]:.<20}R$  ', end='')
    print(f'{listaprodut[prox]}')
    prox += 2
print('_' * 40)
