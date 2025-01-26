# Le nome e preço de varios produtos e mostra, Total de gastos,
# Quantos produtos custam mais de mil reais e Qual nome do produto mais barato.

totalgasto = preco_acima1 = menor_produto = 0
c = {'b': '\033[1;97m'}
print(f'{c['b']}-' * 24)
print('     LOJA SUPER MEN')
print('-' * 24)
while True:
    nomeproduto = parar = preco_produto = produto_nome = ''
    # Testa se Digitou Letra
    while not nomeproduto.isalpha():
        nomeproduto = str(input('Nome do produto:')).strip().capitalize()

    # Testa se Digitou numeros
    while not preco_produto.isnumeric():
        preco_produto = str(input('Preço: R$').strip())

    # Condiçoes do programa
    preco_produto = float(preco_produto)
    totalgasto += preco_produto
    if preco_produto > 1000:
        preco_acima1 += 1
    # menor preço
    if menor_produto == 0:
        menor_produto = preco_produto
    if preco_produto < menor_produto:
        menor_produto = preco_produto
        produto_nome = nomeproduto

    # Teste se digitou S ou N
    while True:
        parar = str(input('Quer continuar? [S/N]')).upper().strip()
        if len(parar) == 0:
            parar = 'A'
        if parar[0] in 'NS' and parar.isalpha():
            break
    if parar[0] == 'N':
        break

print('\033[1;32m---------------COMPRAS FINALIZADAS----------------\033[1;97m')
print(f'Total de gastos somandos todos os produtos, R${totalgasto}')
print(f'Ao todo temos {preco_acima1} no valor acima de mil reais')
print(f'O produto com menor valor foi um {produto_nome} com valor de R${menor_produto}')
