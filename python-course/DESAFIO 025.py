# Programa lê um nome de uma pessoa e diz se o nome dele tem 'SILVA'

nome = str(input('Digite seu nome:'))
print(f'Seu nome tem "SILVA" ?{'SILVA' in nome.upper()}')