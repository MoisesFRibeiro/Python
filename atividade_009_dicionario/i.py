# Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa, delete o último elemento e mostre uma listagem nova.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 04/07/2024
# dicionários

import os


os.system('cls')

# criando um dicionário 
frutas = {}

# atribuindo 4 elementos ao dicionário
frutas[1] = 'maçã'
frutas[2] = 'goiaba'
frutas[3] = 'uva'
frutas[4] = 'morango'

# imprimindo a lista completa
print(f'lista completa de frutas é {frutas}')

# deletando o ultimo elemento
if frutas == '4':
    if meu_dicionário:
         frutas.popitem()
         print(f' ultimo item removido: {frutas}')