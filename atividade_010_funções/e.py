# Crie uma função que receba a altura e o peso de uma pessoa. Depois retorne o seu IMC.

import os


os.system('cls')

print('-'*70)
print('retornando o imc')
print('='*70)

def calcular_imc():
    calculo_imc = peso / (altura * altura) 
    
    return calculo_imc
    
    
altura = float(input('Entre com sua altura (em m): '))
peso = float(input('Entre com o seu peso (em kg): '))

imc = calcular_imc()

print(f'O seu imc é de {imc:.2f}')
print()