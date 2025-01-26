# Programa que pergunte a distancia de uma viagem em Km. Calcula o preço da passagem,
# Cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas

v = int(input('Qual vai ser a distancia da viagem? Km'))
if v > 200:
    p = v * 0.45
    print(f'A viagem vai ter uma distancia de km/h{v} e vai custar R${p:.2f}')
else:
    p = v * 0.50
    print(f'A viagem vai ser de Km/h{v} o preço da viagem vai ser de R${p:.2f}')
