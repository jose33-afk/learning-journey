# Programa que lê o comprimento de três retas e diz ao usuarios se
# Elas podem formar um triângolo.

r1 = float(input('Primeira reta:'))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('A')
print(f'As retas {r1}, {r2} e {r3} Podem formar um Triangolo? )')
