n1 = int(input('\033[32mDigite o primeiro numero:\033[m '))
n2 = int(input('\033[32mDigite o segundo numero:\033[m '))
cores = {'corpadrao':'\033[m', 'branco':'\033[97m'}
s = n1 + n2
print(f'\033[34mA soma entre {cores["branco"]}{n1} e {n2} é {s}{cores["corpadrao"]}\033[m')


