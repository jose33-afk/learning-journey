from utilidades import dado, moeda

p = dado.validacao(valor=input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)