# Soma todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 a 500

smip = 0
ctdi = 0
for n in range(3, 501, 3):
    if n % 2 != 0:
        smip += n
        ctdi += 1

print(f'''
O total de numeros impares multiplos de tres encontrados foi de {ctdi}
Soma de todos impares é {smip}
''')

