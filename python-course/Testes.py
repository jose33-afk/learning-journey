try:   # Vai tentar fazer a operaçao abaixo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):  # caso de erro ele excuta o bloco a baixo
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Nao é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu n informar os dados!')
else:  # opicional
    print(f'a soma entre {a} e {b} é {r}')
finally:  # # opicional sempre vai acontecer
    print('Volte sempre!')