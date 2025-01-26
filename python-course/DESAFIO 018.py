# Programa q lê um angulo e mostra o Seno, Cosseno e tangente desse angolo.

from math import sin, cos, tan, radians
a = int(input('Digite o angolo: '))
s = radians(a)
print(f'O seno do angolo {a}° é {sin(s):.2f}\nO cosseno de {a}° é {cos(s):.2f}\nO tangente de {a}° é {tan(s):.2f}')


