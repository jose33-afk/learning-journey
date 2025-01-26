# Programa que lê o ano de nascimento de jovem e de acordo com sua idade informe,
# Se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou
# Se ja passou da hora.

from math import fabs  # Pegar numero absoluto
from datetime import date  # Pegar data do pc

print('\033[1;32mALISTAMENTO MILITAR')
print('='*30)
sx = str(input('INFORME SEU SEXO M/F:')).upper()

analis = 0
anat = 0
idade = 0
dif = 0

if sx == 'M':
    n = int(input('INFORME SUA DATA DE NASCIMENTO:'))
    analis = n + 18  # ano de alistamento
    anat = date.today().year  # ano atual
    idade = int(fabs(n - anat))  # Idade
    dif = int(fabs(idade - 18))  # Calcula a diferença
    print(f'Voce nasceu em {n}.\npessoas que nasceram nessa data tem {idade} anos em {anat}')
    print('-' * 85)
    if idade == 18:
        print('\033[1;30;42mChegou a hora de se alista!\033[m')
    elif idade < 18:
        print(f'\033[1;30;43mÍnfelismente ainda n esta na hora de se alistar'
              f' mais n desanime, faltam so {dif} anos!\033[m\n\033[1;30;43mSeu alistamento sera em {analis}\033[m')
    elif idade > 18:
        print(f'\033[1;30;41mVoce ja passou da hora de se alistar ha {dif} '
              f'anos, corra e va agora!\033[m\n\033[1;30;41mSeu alistamento foi em {analis}\033[m')
elif sx == 'F':
    print('\033[32m-' * 85)
    print('\033[1;30;42mVoce n é obrigada a fazer o alistamento militar.'
          '\033[1;30;42mTenha um Bom dia!\033[m')
print('\033[32m-' * 85)
