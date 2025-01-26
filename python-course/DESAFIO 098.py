# Mostra uma contagem de 1 ate 10 de 1 em 1, de 10 ate 0, de 2 em 2 e
# Um contagem personalizada

from time import sleep


def esc():
    print('-=-'*15)


def contagem(i, f, p):
    # Contagem regressiva
    if p < 0:
        p = abs(p)
    elif p == 0:
        p = 1
    print(f'Contagemde de {i} até {f} de {p} em {p}')
    if i > f:
        print(i, end=' ')
        while i >= f:
            i -= p
            if i < f:
                break
            print(i, end=' ')
            sleep(0.3)
    else:
        while i <= f:
            print(i, end=' ')
            sleep(0.3)
            i += p
    print('FIM!')


# Principal
esc()
contagem(1, 10, 1)
esc()
contagem(10, 0, -2)
esc()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
