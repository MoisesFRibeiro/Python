# Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

import os
import random


os.system('cls')

print('-'*70)
print(' adivinhação')
print('='*70)

print('numero aleatorio inteiro')

numero = int(input('entre com o numero '))
aleatorio_inteiro = random.randint(1,5)

if aleatorio_inteiro == numero:
    print(f'parabens {numero} é igual a {aleatorio_inteiro}')

else:
    print(f'errou o numero digitado foi {numero} o numero pensado foi {aleatorio_inteiro}')    