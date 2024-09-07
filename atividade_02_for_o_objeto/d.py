# Faça um programa que imprima os números pares entre 0 e 100.
import os


# Classe
class Pares:
    # Método construtor
    def __init__(self, numeros_pares,):
        self.numeros_pares = numeros_pares

    # Entrada de dados
    numeros_pares = (0, 100)

    #  Método para realizar a contagem de numeros pares
    for var in range(0, 100):
        numeros_pares = numeros_pares
        if(numeros_pares % 2 == 0):
            print(f'os numeros primos pares são:{numeros_pares} ')  
            