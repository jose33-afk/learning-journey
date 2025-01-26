m = float(input('\033[1;36mDigite a medida em \033[32mM(s)\033[1;36m para  converter:'))
print(f'\033[1;32m{m:.0f}m\033[1;97m convertido em kilometros, \033[1;37m{m/10/10/10:.3f}Km\033[m')
print(f'\033[1;32m{m:.0f}m\033[1;97m convertido em Hectometro, \033[1;31m{m/10/10:.5f}hm\033[m')
print(f'\033[1;32m{m:.0f}m\033[1;97m convertido em Decametro, \033[1;32m{m/10:}dam\033[m')
print(f'\033[1;32m{m:.0f}m\033[1;97m convertido em decimetro, \033[1;33m{m*10}dm\033[m')
print(f'\033[1;32m{m:.0f}m\033[1;97m convertido em centimetros, \033[1;34m{m*10*10}cm\033[m')
print(f'\033[1;32m{m:.0f}m\033[1;97m convertido em milimetros, \033[1;35m{m*10*10*10}mm\033[m')


