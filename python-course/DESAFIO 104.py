# Cria uma funçao que so aceita numeros

def leiaint(n):
    print('---' * 15)
    while True:
        n = str(input('\033[1;97mDigite um número:')).strip()
        if n.isnumeric():
            return n  # return aparetemente funciona com um breker no while, n testei no for
        print('\033[1;31mERRO! Digite um número inteiro válido!')


# Principal
num = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {num}')