# Programa que pergunta a quantidade de Km percorrido por um carro alugado e a quantidade de dias
# pelos quais foi alugado. Calcula o preço a pagar, R$60 por dia e R$0.15 por Km rodado

dia = int(input('Quantos dias Alugado?'))
km = float(input('Quntos quilometros foi rodado ? Km'))
p = km * 0.15 + dia * 60
print(f'Total a pagar R${p:.2f}')
