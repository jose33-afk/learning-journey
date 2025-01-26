# Pode ou n fazer um emprestimo. se o valor da parcela mesal for 30% do salario
# do usuario, o usuario n pode fazer o emprestimo.

from time import sleep

vlc = float(input('Qual valor da casa que deseja comprar:R$'))
print('\033[1;33mPara proseguirmos preciso de mais algumas informaçoes suas.\033[m')
slc = float(input('Qual é o seu salario mensal:R$'))
print('\033[1;33mSo mais uma pergunta e podemos dizer se voce pode ou n pegar o emprestimo.\033[m')
anpt = int(input('Em quantos anos pretende pagar:Anos'))
print('\033[33mProcessando os dados... Aguarde.')

sleep(1.5)
n = anpt * 12
p = vlc / n  # Valor da parcela mensal
porl = (30*slc) / 100  # 30% do salario

print('RESULTADO..')
if p >= porl:
    print('\033[1;31m=-='*16)
    print('\033[1;30;41mNEGADO\033[m')
    print('Infelismente n podemos aceitar seu imprestimo,\nvoce n conseguia arcar com as parcelas mensais.')
    print('\033[1;31m=-=' * 16)
elif p < porl:
    print('\033[1;32m=-=' * 16)
    print('\033[1;30;42mACEITO\033[m')
    print('\033[1;32mParabens! seu imprestimo foi aceito com sucesso!\033[m')
    print(f'\033[1;32mPara pagar o emprestimo de R${vlc} em {anpt} anos as parcelas serao de R${p:.2f}')
    print('\033[1;32m=-=' * 16)


