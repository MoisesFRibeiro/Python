# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores. 
import os

# Classe 
class Valor:
    # Método Construtor 
    def __init__(self, valor_1, valor_2, valor_3 ):
        self.valor_1 = valor_1
        self.valor_2 = valor_2
        self.valor_3 = valor_3 

    # Método para classe somar
    def somar(self, valor_1 , valor_2, valor_3):
        self.somar  valor_1 + valor_2 + valor_3
        return somar

    # método para classe multiplicar
    def multiplicar(self, valor_1, valor_2, valor_3):
        self.multiplicar valor_1, valor_2, + valor_3
 
# Entrada de dados
valor_1 = input('digite o valor 1: ')
valor_2 = input('digie o valor 2: ')
valor_3 = input('digite o valor 3: ')

# invocando o método somar e multiplicar
resultado_soma = somar(valor_1, valor_2, valor_3)
resultado_multiplicar = multiplicar(valor_1, valor_2, valor_3)

print(f'calculo da soma: {resultado_soma}')
print(f'calculo da multplicação {resultado_multiplicar}')