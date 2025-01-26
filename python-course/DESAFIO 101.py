# Cria uma funçao chamada voto que retorna, literal negado, opcional
# ou obrigatorio, com o parametro ano nascimento


def voto(ano=0):
    from datetime import date  # importaçao local só funciona aqui dentro
    if ano == 0:
        return '\033[1;31mERRO! você não informou o ano de nascmento'
    else:
        idade = date.today().year - ano
        print(f'Com {idade} anos:', end=' ')
        if idade > 65 or 16 <= idade < 18:
            return 'VOTO OPICIONAL.'
        elif idade >= 18:
            return 'VOTO OBRIGATORIO.'
        elif idade < 16:
            return 'NÃO VOTA.'


print('---'*15)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
