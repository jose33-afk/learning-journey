print('CONVERSOR DE NUMERO')
n = int(input('Digite um numero:'))
print('''==============================
Digite [1] para binario      |
Digite [2] para octal        |
Digite [3] para hexadecilmal |
==============================
      ''')
opc = int(input('Digite sua opçao:'))
if opc == 1:
    print(f'O numero {n} em binarios é {bin(n)[2:]}')
elif opc == 2:
    print(f'O numero {n} em octal é {oct(n)[2:]}')
elif opc == 3:
    print(f'O numero {n} em hexadecimal é {hex(n[2:])}')
else:
    print('ERRO')
