# Cria uma funcao que analiza o maior valor entre varios numeros

from time import sleep


def maior(*v):
    print('-=-'*15)
    print('Analizando valores passados...')
    for c in v:
        print(c, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(v)} ao todo.')
    m = 0
    for c in v:
        if c > m:
            m = c
    print(f'O maior valor informado foi {m}.')


# Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('-=-'*15)
