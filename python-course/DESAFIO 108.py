# adapte o ex107 adicionando, uma funçao chamda moeda
# Que mostra os valores monetarios formatados

from utilidades import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))} Reais.')
print(f'O dobro de R${p} é R${moeda.moeda(moeda.dobro(p))} Reais.')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
