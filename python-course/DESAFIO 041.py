# Classifica a categoria de um atleta, Mirim, Infantil, junhor
# senior, master

from time import sleep  # tempo de resposta
from datetime import date  # data
dtn = int(input('Qual ano de nascimento do atleta? '))
print('\033[1;32mCalculando Categoria... Aguarde..\033[m')
sleep(1.5)
dta = date.today().year  # Data atual
idd = dta - dtn  # idade
print(f'Voce tem {idd} anos, Sua categoria é.')  # Ano do atleta
cg = ''
a = ''
if idd <= 9:
   a = '\033[1;30;107mmirim'
   cg = '\033[1;97m'
elif idd <= 14:
    a = '\033[1;30;47mInfantil'
    cg = '\033[1;37m'
elif idd <= 19:
    a = '\033[1;30;44mJunor'
    cg = '\033[1;34m'
elif idd <= 25:
    a = '\033[1;97;40mSenior'
else:
    a = '\033[1;30;41mMASTER'
    cg = '\033[1;31m'
print(f'{cg}='*30)
print(f'{a}                         \033[m')
print(f'\033[m{cg}='*30)


