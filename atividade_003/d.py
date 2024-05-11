# Faça um programa que receba um ângulo qualquer. Em seguida, calcule o seno, cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.

import os
import math


os.system('cls')

angulo = float(input('entre com o angulo'))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'o seno {angulo} é: {seno:.2f}')
print(f'o cosseno{angulo} é: {cosseno:.2f}')
print(f'a tangente de {angulo} è: {tangente:.2f}')