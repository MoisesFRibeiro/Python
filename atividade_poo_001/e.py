# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
import os 

# Classe
class Numero_inteiro:
    # Método Construtor
    def __init__(self, inteiro, sucessor, antecessor):
        self.inteiro =  inteiro
        self.sucessor = sucessor
        self.antecessor = antecessor

    # Método para receber o número inteiro e verificando antecessor e sucessor
    ineiro = input('digite o numero inteiro: ')
    antecessor = -1
    sucessor = + 1

# Exibindo o antecessor e o sucessor
print(f'o valor do antecessor: (antecessor)')
print(f'o valor do sucessor é: (sucessor)')

