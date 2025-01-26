# Lê nome e media de um aluno tudo guadado em um dicionario

aluno = dict()
aluno['nome'] = str(input('\033[1;97mNome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}:'))

# Situaçao da média
if aluno['media'] >= 7:
    aluno['performance'] = '\033[1;32mAprovado'
elif 5 <= aluno['media'] < 7:
    aluno['performance'] = '\033[1;33mRecuperaçao'
else:
    aluno['performance'] = '\033[1;31mReprovado'

# mostrando
print('-=-'*20)
for indece, elementos in aluno.items():
    print(f'- {indece} é igual a {elementos}')
