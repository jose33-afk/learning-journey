# Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triangolo
# retagulo, calcula e mostra o comprimento da hipotenusa

from math import sqrt, pow
op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
r = sqrt(pow(op, 2)+pow(ad, 2))
print(f'Comprimento da hipotenusa é {r:.2f}')
