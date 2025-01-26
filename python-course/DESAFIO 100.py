# cria duas funçoes uma que sorteia 5 numeros e poe em uma lista e,
# somapar que soma os pares dessa lista.

from random import randint
from time import sleep


def prenche(li):
    # Sorteia 5 numeros
    print('Sorteando 5 valores da lista:', end=' ')
    for p, v in enumerate(range(5)):
        li.append(randint(1, 10))
        print(li[p], end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(li):
    # soma os numeros pares da lista
    sp = 0
    for lis in li:
        if lis % 2 == 0:
            sp += lis
    print(f'Somado os valores peres {numeros}, temos {sp}')


# Principal
numeros = []
prenche(numeros)
somapar(numeros)
