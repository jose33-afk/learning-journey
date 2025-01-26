# Programa que pergunta o salario de um funcionario e calcula
# o valor do seu aumento, Para salários superiores a R$ 1.250,00, calcula um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

nome = str(input('Qual nome do funionario? ')).strip().capitalize()
s = float(input(f'Qual salario de {nome} R$'))
if s > 1250:
    ns = s + (10*s) / 100
else:
    ns = s + (15*s) / 100
print(f'O novo salario de {nome} é de R${ns}')
