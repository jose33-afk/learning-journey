def calcarea(m, c):
    print(f'A área de um terreno {metrs}x{compri} é de {m*c}m².')


# Principal  calcula a área
print(' Controle de terrenos ')
print('--'*11)
metrs = float(input('LARGURA (m):'))
compri = float(input('COMPRIMENTO (m):'))
calcarea(metrs, compri)
