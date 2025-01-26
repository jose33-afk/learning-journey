# Cria funcao fatoria que mostra o fatoria do numero pedido
# A funcao tem um parametro opcional que mostra ou n o processo


def fatorial(num=0, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param num: O número a ser calculado.
        :Para show:(opcional) Mostra ou não a conta.
    """
    if show == True:
        fi = 1
        for c in range(num, 0, -1):
            fi *= c
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        print(fi)
    else:
        fi = 1
        for c in range(num, 0, -1):
            fi *= c
        print(f'O fibonacci de {num} é {fi}')


print('---'*15)
fatorial(5)

