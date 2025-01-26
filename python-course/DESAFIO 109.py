# adapte o ex107 para que ela aceite um parametro a mais

from utilidades import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)} Reais.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)} Reais.')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% temos {moeda.diminuir(p, 13, True)} Reais')