# Programa q analiza se o ano digitado é bissexto

ano = str(input('Digite um ano q gostaria de saber se vai ser bissesxto: ')).strip()
c = len(ano)
print('='*30)
if c == 8:
    cl = int(ano[4:9])
    ano = str(f'{ano[:2]}/{ano[2:4]}/{ano[4:]}')
    if cl % 4 == 0 and cl % 100 != 0 or cl % 400 == 0:
        print(f'O {ano} é bissexto!')
    else:
        print(f'O ano {ano} n é bissexto')
elif c == 4:
    cl = int(ano[0:5])
    if cl % 4 == 0 and cl % 100 != 0 or cl % 400 == 0:
        print(f'O {ano} é bissexto!')
    else:
        print(f'O ano {ano} n é bissexto')
print('='*30)
