# Programa que lê duas notas de um aluno e calcula sua media, mostrando
# Uma messangem no final, de acordo com sua media

c = {'nm': '\033[m', 'am': '\033[1;33m', 'az': '\033[1;34m', 'cz': '\033[1;37m'}  # cores
nal = str(input(f'{c['cz']}Informe o nome do aluno(a):')).capitalize().strip()
not1 = float(input(f'{c['az']}Digite a primeira nota de {nal}: '))
not2 = float(input(f'{c['az']}Digite a segunda nota de {nal}{c['nm']}: '))
m = (not1 + not2) / 2  # media
rst = '0'  # pra variavel funcionar fora e dentro do if, se n declarar antes da erro n sei pq.
cal = '0'
if m < 5.0:
    rst = '\033[1;30;41mREPROVADO'
    cal = '\033[1;31m'  # cor do resultado
elif 5.0 <= m <= 6.9:
    rst = '\033[1;30;43mRECUPERAÇAO'
    cal = '\033[1;33m'
elif m >= 7.0:
    rst = '\033[1;30;42mAPROVADO'
    cal = '\033[32m'
print(f'RESULTADO')
print(f'{cal}-=-{c['nm']}'*10)
print(f'{cal}O aluno(a):{nal}.')
print(f'Nota, {m:.1f}')
print(f'{cal}-'*30)
print(f'{rst}')
print(f'\033[m{cal}-=-{c['nm']}'*10)
