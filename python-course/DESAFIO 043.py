# Lê peso e altura e calcula e mostra o IMC

from time import sleep #tempo
#importaçao
print('\033[1;37mCALCULO DO IMC')
print('='*30)
al = float(input('\033[1;34mDigite sua altura (m):'))
ps = float(input('Agora  seu peso (kg): Kg\033[m'))
print('\033[1;33mCalculando seu IMC...')
sleep(1.5)#Pausa de 1.5 seg
imc = ps / (al*al) #Calculo do imc
print('\033[1;37m-'*30)
print(f'Seu imc é de \033[1;35m{imc:.2f}')
print('\033[1;37m-'*30)
#Condiçoes
if imc < 18.5:
    print('\033[1;30;43mAbaixo do peso!!!!')
elif 18.5 <= imc < 25:
    print('\033[1;30;42mPESO IDEAL')
elif 25 <= imc < 30:
    print('\033[1;30;44mSOBREPESO!!')
elif 30 <= imc < 40:
    print('\033[1;30;41mOBSIDADE!!!')
else:
    print('\033[1;97;40mOBSIDADE MORBIDA!!!!')

