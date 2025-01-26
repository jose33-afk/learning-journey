# Criar um modulo com as funçoes, metade, dobro, aumentar e dimunir

from utilidades import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p):.2f} Reais.')
print(f'O dobro de R${p} é R${moeda.dobro(p):.2f} Reais.')
print(f'Aumentando 10% temos R${moeda.aumentar(p, 10)} Reais')
print(f'Reduzindo 13%, temos R${moeda.diminuir(p, 13)} Reais')
