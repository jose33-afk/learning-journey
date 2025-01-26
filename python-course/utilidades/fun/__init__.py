def testidade():
    """
    :return: Retorna um valor int, e só sai quando for um int válido.
    """
    p = 0
    while True:
        try:
            p = int(input('Idade: '))
            return p
        except ValueError:
            print(f'{c('r')}ERRO: por favor, digite uma idade válida.{c('w')}')


def testestring():
    """
    :return: Quando a variavel nome, for somente string
    """
    while True:
        nome = str(input('Nome:')).strip().capitalize()
        copia = nome
        nome = nome.replace(' ', '')
        if nome.isalpha():
            nome = copia
            return nome
        print(f'{c('r')}ERRO! Por Favor Digite somente Letras no nome!{c('w')}')


def c(co='n'):
    """
    :param co: escolha do usuario
    :return: retorna a cor escolhida
    """
    cor = {'n': '\033[1;m',
           'p': '\033[1;30m',
           'r': '\033[1;31m',
           'g': '\033[1;32m',
           'y': '\033[1;33m',
           'z': '\033[1;34m',
           'c': '\033[1;36m',
           'w': '\033[1;97m'
           }
    for k, v in cor.items():
        if k in co:
            return v