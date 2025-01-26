c = float(input('Quantos reais vc tem para converter na carteira R$? '))
print(f'\033[1;34mR${c:.2f} convertido em dolar US$\033[1;32m {c/5.09:.2f}')
print(f'\033[1;31mR${c:.2f} convertido em Yen \033[32m{c*30.13:.2f}YPY$\n\033[1;33mR${c:.2f} convertido em Euro \033[1;32m{c/5.56:.2f}EUR$')
