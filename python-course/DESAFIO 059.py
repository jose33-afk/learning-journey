# Programa que le dois valores e mostra um menu de opçoes.

valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
print('-' * 30)

soma = multipro = maior = escolha = 0

while escolha != 5:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa')
    print('-' * 30)
    escolha = int(input('Qual opçao deseja? '))
    print('=' * 30)

    if escolha == 1:
        soma = valor1 + valor2
        print(f'A soma dos dois numeros é {soma}.')
    elif escolha == 2:
        multipro = valor1 * valor2
        print(f'Multiplicando {valor1} x {valor2} = {multipro}')
    elif escolha == 3:
        maior = valor1
        if maior < valor2:
            maior = valor2
        print(f'Entre {valor1} e {valor2} o maior é {maior}')
    elif escolha == 4:
        valor1 = int(input('Digite o primeiro valor novo:'))
        valor2 = int(input('Digite o segundo valor novo:'))
    elif escolha == 5:
        print('Saindo do programa...')
    else:
        print('Erro tente novamente!')
    print('=' * 30)
