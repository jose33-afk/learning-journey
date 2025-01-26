# Programa que lê a velocidade de um carro, se ele ultrapassar 80Km, mostre
# uma menssagem dizendo que ele foi multado, a multa vai custar R$7,00 or cada km acima do limite.

v = int(input('Qual foi a velocidade do veiculo? Km'))
if v > 80:
    d = (v - 80) * 7
    print(f'Veiculo acima de 80km/h você foi multado no valor de R${d:.2f}')
print('Velocidade permitida nada de errado!')
