# Primo ou n primo

print('\033[1;97mÉ um numero primo ou n?')
print('-'*20)
num = int(input('Digite um numero:'))
print('-'*20)

cvz = 0

for c in range(1, num+1):  # Quantas vezes o numero é dividido
    if num % c == 0:
        print(f'\033[1;32m{c} ', end='')
        cvz += 1
    else:
        print(f'\033[1;31m{c} ', end='')

if cvz == 2 and num % num == 0 and num % 1 == 0:  # Teste se é primo ou n
    print('\n'
          f'\033[1;33mO numero \033[1;97m{num}\033[1;33m é \033[1;30;42mPRIMO\033[m\033[1;33m!')
else:
    print('\n'
          f'\033[1;33mO numero \033[1;97m{num} \033[1;30;41mNAO\033[m\033[1;33m é '
          f'PRIMO por ser divisivel \033[1;97m{cvz}\033[1;33m vezes!')
    
