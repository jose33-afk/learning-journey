# Programa que lê o nome completo de uma pessoa, mostra em seguia
# o primeiro e o ultimo nome separadamente

nome = str(input('Digite seu nome completo:')).strip().split()
c = len(nome)
print(f'Seu primeiro nome é, {nome[0].capitalize()}')
print(f'Seu ultimo nome é, {nome[c-1].capitalize()}')