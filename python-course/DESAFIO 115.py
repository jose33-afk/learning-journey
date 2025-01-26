# Sistema de modularizadom que permite cadastrar pessoas pelo nome e idade,
# Em um arquio de txt

from utilidades.fun import testidade, testestring, c


def menu():
    print(f'-{c("w")}' * 50)
    print(f'{"MENU PRINCIPAL":^49}')
    print('-' * 50)
    print(f'{c("y")}1{c("w")} - {c("z")}Ver pessoas cadastradas')
    print(f'{c("y")}2{c("w")} - {c("z")}Cadastrar nova Pessoa')
    print(f'{c("y")}3{c("w")} - {c("z")}Sair do Sistema')


def mostra():
    print(f'{c("w")}-' * 50)
    print(f'{"PESSOAS CADASTRADAS":^49}')
    print('-' * 50)
    with open('teste_manip.txt', 'r', encoding='utf-8') as t:
        t = t = t.read()
    print(t)


def cadastra(nome='', idade=0):
    with open('teste_manip.txt', 'a') as a:
        a.write(f'\n{nome:40}{idade} Anos')
    print(f'{c('g')}-' * 50)
    print(f'Novo registro de {nome} adicionado!')
    print(f'-' * 50, c('n'))


# Principal
while True:
    opc = 0
    menu()
    # Testa se a opçao está correta
    while True:
        try:
            opc = int(input(f'{c("y")}Sua opçao:'))
            if 1 <= opc <= 3:
                break
        except ValueError:
            print(f'{c(["r"])}EROO! A opçao selecinada n existe!{c(["w"])}')
        else:
            print(f'{c('r')}ERRO! Digite uma opçao Válida!{c('w')}')

    # Opçao selecionada
    if opc == 1:
        mostra()
    elif opc == 2:
        print(f'{c(["w"])}-' * 50)
        print(f'{"NOVO CADASTRO":^49}')
        print('-' * 50)
        n = testestring()
        i = testidade()
        cadastra(n, i)
    elif opc == 3:
        print(f'{c(["g"])}-' * 50)
        print(f'{"Saindo do sistema... Até logo!":^49}')
        print('-' * 50)
        break
