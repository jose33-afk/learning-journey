n = int(input('\033[30;42mDigite um numero:\033[m '))
a = {'A':'\033[1;30;45m'}
print(f'{a["A"]}Dobro de \033[97m{n}{a["A"]}{a["A"]} é \033[1;32m{n+n}\033[m{a["A"]} e o triplo de \033[97m{n}{a["A"]} é \033[1;32m{n*3}{a["A"]}\033[m')
print(f'{a["A"]}A Raiz quadrada de \033[1;97m{n}{a["A"]} é \033[1;32m{n**(1/2):.2f}\033[m')
