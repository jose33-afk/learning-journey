# funçao notas(), quantidade de notas, a maior nota, a menor nota, a media da turma
# a situaçao (opcional)

def notas(*no, sit=False):
    """
        ->Funçao para analizar varias notas de alunos
        :no:notas
        :sit=True: adiciona a situaçao dos alunos
        :return:Ele vai retornar em forma de dicionarios, algumas informaçoes dos alunos
    """
    aux = 0
    for p, nts in enumerate(no):
        aux += nts
    media = aux / len(no)
    if media > 7:
        sita = 'BOA'
    elif 5 <= media < 7:
        sita = 'Razóavel'
    else:
        sita = 'RUIM'
    alunos = {'total': len(no), 'Maior': max(no), 'Menor': min(no), 'Média': media}
    if sit:
        alunos['situaçao'] = sita
    return alunos.copy()


print('---'*20)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
help(notas)
