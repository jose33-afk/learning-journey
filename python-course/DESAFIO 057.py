# Programa q le o sexo de uma pessoa e se ela digitar algo que n seja
# M ou F , o programa repete ate digitar F ou M corretamente

sexo = str(input('\033[1;37mDigite seu sexo [M/F]')).upper().strip()
print('\033[1;33m-'*30)

segr = ''

if sexo != 'M' and sexo != 'F':
    while not sexo == 'M':
        sexo = str(input('\033[1;33mQual seu sexo ESCOLHA F, feminino ou M, masculino:')).upper()
        if sexo != 'F' and sexo != 'M':
            print(f'\033[1;31mERRO N EXISTE SEXO {sexo}')
        else:
            if sexo == 'F':
                segr = 'F'
                sexo = 'M'
                print(f'\033[1;33mSexo [{segr}] selecionado!')
            else:
                segr = 'M'
                print(f'\033[1;33mSexo [{segr}] selecionado!')
else:
    print(f'\033[1;33mSexo [{sexo}] selecionado!')

