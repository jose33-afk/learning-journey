#with open(nome_arquivo, objetivo de abrir o arquivo) #with abre e fecha o arquivo

with open('email.txt', 'r') as arquivo:
    gmail = arquivo.read()                # read pega usar quando o arquivo tiver so uma linha

print(gmail)

with open('mensagem.txt', 'r', encoding='utf-8') as msg:  # encoding, corrige bugs com caracteres especias
    s = msg.readlines()

for linha in s:
    if 'faturamento' in linha:
        print(linha)

with open('senhatestes.txt', 'w') as arg:  # W cria arquivo se n exitir, ou se ja existir troca o conteudo
    arg.write('rita')

with open('email.txt', 'a') as g: # A adiciona uma informaçao, ou cria um arquivo se n existir
    g.write('\ncesar') # usar \n pra pular linha se nao fica tudo junto

with open('email.txt') as g:
    g = g.read()
print(g)
