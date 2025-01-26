# Programa lê o nome de uma pessoa e mostra, O nome com todas as letras Maiusculas,
# Letras minusculas, Quantas letras tem o nome sem considerar os espaços e quantas letras tem o primeiro nome

frase = input('Digite seu nome completo:').strip()
print(f'Seu nome em letras Maiusculas, {frase.upper()}')
print(f'Seu nome em letras Minusculas, {frase.lower()}')
print(f'Quantidade de letras do seu nome é, {len(frase.replace(' ', ''))}')
frase = frase.split()
print(f'Seu primeiro nome é {frase[0]} e ele tem {len(frase[0].strip())} letras')

