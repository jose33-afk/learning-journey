def f(n):
    c = len(n) + 4
    print('-'*c)
    print(f'  {n.upper()}')
    print('-'*c)


# Principal poe duas linhas em baixo e em cima de um flase ou palavra
nome = str(input('Digite um nome para ser formatado: '))
f(nome)
