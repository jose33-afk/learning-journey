# Calcula um preço de um produto dependendo da forma de pagamento, A vista:Dinheiro/cheque 10% de desconto,
# A vista no cartao 5%, em ate 2x no cartao preço normal e 3x ou mais no cartao 20% de juros

c = {'nm': '\033[m', 'cz': '\033[1;37m', 'vd': '\033[1;32m', 'bc': '\033[1;97m',  # cores
     'am': '\033[1;33m', 'az': '\033[1;34m', 'pv': '\033[1;30;42m', 'vm': '\033[1;31m'}

vdp = float(input(f'{c['bc']}Informe o valor do produto: R$'))  # inicio
print(f'Qual vai ser a forma de pagamento', end='')
cv = int(input(f'[{c['vd']}AVISTA[1]{c['am']}{c['bc']}|OU|{c['am']}CARTAO[2]{c['bc']}]:'))
# Condiçoes

fmp = '0'  # Escolha
vl = '0'  # Valor parcela
vzs = '0'

if cv == 1:
    print(f'{c['bc']}-' * 50)
    print(f'{c['az']}Pagando a vista voce ganha um desconto de 10%!!{c['nm']}')  # Dinheiro/Cartao
    print(f'{c['bc']}-' * 50)
    print(f'{c['cz']}[{c['vd']}Dinheiro[D]{c['cz']}/{c['bc']}', end='')
    fmp = str(input(f'Cheque[C]{c['nm']}{c['cz']}{c['cz']}]:')).upper().strip()
elif cv == 2:
    print(f'{c['bc']}-' * 85)
    print(f'{c['az']}Pagando em 1x no Cartao ganha 5% de desconto, 2x preço normal e 3x ou mais tem 20% de juros.')
    print(f'{c['bc']}-' * 85)
    print(f'{c['am']}Deseja pagar de {c['bc']}1x{c['am']} no cartao Digite', end='')
    print(f'{c['bc']} (1){c['am']},{c['bc']} 2x {c['am']}Digite{c['bc']} (2)', end='')
    fmp = str(input(f'{c['nm']}, {c['bc']}3x{c['am']} ou mais vezes digite {c['bc']}(3){c['am']}:'))
    if fmp == '3':
        vzs = int(input('Quantas vezes deseja pagar? x'))
        print(f'{c['bc']}-' * 85)
else:
    print(f'{c['vm']}ERRO OPÇAO INVALIDA TENTE NOVAMENTE')

if fmp == 'D' or fmp == 'C':
    print(f'{c['vd']}=' * 85)
    print(f'{c['pv']}Pagando a vista seu produto sai por R${vdp - (10 * vdp) / 100:.2f}{c['nm']}')  # Desconto
    print(f'{c['vd']}=' * 85)
elif fmp == '1':
    print(f'{c['vd']}=' * 85)
    print(f'{c['pv']}Pagando em 1x vezes no Cartao seu produto sai por R${vdp - (5 * vdp) / 100:.2f}{c['nm']}')
    print(f'{c['vd']}=' * 85)
elif fmp == '2':
    print(f'{c['vd']}=' * 85)
    print(f'{c['pv']}Pagando em 2x vezes no Cartao seu produto sai por R${vdp:.2f}{c['nm']}')
    print(f'{c['vd']}=' * 85)
elif fmp == '3':
    vl = vdp + (20 * vdp) / 100
    v = vl / vzs
    print(f'{c['pv']}Pagando em {vzs}x vezes de R${v:.2f} seu produto sai por R${vl:.2f}{c['nm']}')
    print(f'{c['vd']}=' * 85)
