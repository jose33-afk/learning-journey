# Pede q digite tres lados de um triangolo, analiza se pode formar um trianolo,
# se sim, mostra se é um triangolo equilatero, escaleno ou isosceles

print('\033[1;33mANALIZADOR DE TRIANGOLOS')
print('\033[1;37m-'*25)
l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
print('\033[1;37m-'*25)
if l3 + l2 > l1 and l3 + l1 > l2 and l2 + l1 > l3:
   print(f'\033[1;30;42mO primeiro lado ({l1}), Segundo ({l2}) e o Terceiro ({l3}) podem formar um triangolo!\033[m')
   print('\033[1;37m-' * 25)
   print('E sera um triangolo.')
   if l1 == l2 == l3:
       print('\033[1;30;45mEquilatero\033[m')
   elif l1 == l2 or l1 == l3 or l2 == l3:
       print('\033[1;30;46mIsoceles\033[m')
   else:
       print('\033[1;30;44mEscaleno\033[m')
else:
    print(f'\033[1;30;41mOs tres lados digitados n podem formar um triangolo!\033[m')
print('\033[1;37m-' * 25)
