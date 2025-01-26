# ex112

from utilidades import moeda


def validacao(valor):
    """
    :param valor: a ser verificado
    :return: retorna uma tabela com a funçao formataçao
    """
    valor = str(valor).strip()
    copia = ''
    pos = 0
    while True:
        # if para n dar problema com o replece
        if ',' in valor or '.' in valor:   # Primeiro o que quer procurar vem primeiro.
            # Testando se n tem os dois '.' e o ',' não pode ter.
            for v in valor:  # Não funciona pra valores na casa dos milhoes
                if v == '.':
                    pos += 1
                if v == ',':
                    pos += 1
            if pos == 1:
                # Copiando valor, para caso ele esteja certo.
                if ',' in valor:
                    copia = valor.replace(',', '.')
                else:
                    copia = valor
                # Removendo pontos e virgula, para a validaçao do isnumeric().
                valor = valor.replace(',', '.').replace(' ', '.').replace('.', '')

        # Verificando se foi digitado somente numeros
        if valor.isnumeric():
            if len(copia) == 0:   # caso o valor esteja correto e passe de primeira.
                copia = float(valor)
            copia = float(copia)  # não passou de primeira e ficou em loop.
            return copia
        print(f'\033[31mERRO: "{valor.strip()}" é um preço inválido!\033[m')
        valor = str(input('Digite um preço: R$'))


def testint():
    """
    :return: Retorna um valor int, e so sai quando for int
    """
    while True:
        try:
            p = int(input('Digite um numero Inteiro: '))
        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\nO usuario parou o programa')
            break
        else:
            break


def testefloat():
    """
       :return: Retorna um valor int, e so sai quando for Float
       """
    while True:
        try:
            p = float(input('Digite um numero Real: '))
        except ValueError:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\nO usuario parou o programa')
            break
        else:
            break

