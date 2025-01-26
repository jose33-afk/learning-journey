# Analizar se uma expressao matematica está certa

formula = list(str(input('\033[1;97mDigite a expressão: ')))

# Analizar
a = formula.count('(')
b = formula.count(')')

if a == b:
    print('\033[1;32mSua expressão está certa!')
elif a != b:
    print('\033[1;31mSua expressão está errada!')
