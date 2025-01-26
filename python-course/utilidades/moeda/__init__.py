# Modulo de tratamento de dinheiro, usado ex107, ex108, ex109, ex110

def aumentar(valor=0, por=0, form=False):
    """
    :valor: valor a ser calculado a porcetagem
    :por: porcetagem escolhida
    :return: retorna o valor mais a pocetagem escolhida
    :form: True retorna o valor ja formatado em dinheiro
    """
    r = valor + (valor * por/100)
    if form:
        r = moeda(r)
    return r


def diminuir(valor=0, por=0, form=False):
    """
    :form: True retorna o valor formatado em forma dinheiro
    :valor: valor a ser calculado a porcetagem
    :por: porcetagem escolhida
    :return: retorna o valor menos a pocetagem escolhida
    """
    r = valor - (valor * por/100)
    if form:
        r = moeda(r)
    return r


def dobro(valor=0, form=False):
    """
    :param valor: calculo
    :param form: formataçao
    :return:dobro do valor
    """
    v = valor * 2
    if form:
        v = moeda(v)
    return v


def moeda(valor=0, moed='R$'):
    """
    :param valor:a ser formatado
    :param moed: formato em dinheiro (R$, USS$)
    :return:Retorna o valor formatado
    """
    f = f'{moed}{valor:.2f}'.replace('.', ',')
    return f


def metade(valor=0, form=False):
    """
    :param valor: para o calculo
    :param form: com ou sem formataçao
    :return: Retorna a metade do valor
    """
    v = valor / 2
    if form:
        v = moeda(v)
    return v


def resumo(valor=0, aum=0, redu=0):
    """
    :param valor: Valor a ser analizado
    :param aum: porcentagem que o valor vai aumentar
    :param redu: porcetagem que o valor vai reduzir
    :return: Retorna tabela com as analizes a baixo
    """
    print('---'*11)
    print(f'{"RESUMO DO VALOR":^33}')
    print('---' * 11)
    print(f'{"Preço analizado:":21}{moeda(valor)}')
    print(f'{"Dobro do preço:":21}{dobro(valor, True)}')
    print(f'{"Metade do preço:":21}{metade(valor, True)}')
    print(f'{f"{aum}% de aumento:":21}{aumentar(valor, aum, True)}')
    print(f'{f"{redu}% de reduçao:":21}{diminuir(valor, redu, True)}')
    print('---' * 11)






