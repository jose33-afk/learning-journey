# Tupla com varias palavras, mostra para cada palavra, quais sao as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
rep = espa = 0
for i in range(0, len(palavras)):
    print(f'Na palavra {palavras[i].upper()} temos', end=' ')
    for c in range(0, 5):
        if vogais[c] in palavras[i]:
            for rep in range(0, palavras[i].count(vogais[c])):
                print(vogais[c], end=' ')
    print('')
