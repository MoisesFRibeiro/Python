# Faça um programa que imprima os números no intervalo entre 1 e 100.
#  Os números devem ser apresentados na horizontal.
import os 


# classe
class Horizontal:
    # Método construtor
    def __init__(self, Inicial, Final):
        self.Inicial = Inicial
        self.Final = Final

        
# Método para realizar a contagem       
    def intervalo(self):

        for j in range(self.Inicial, self.Final +1):
            print(f'{j}', end=" | ")

# Criando uma instância
intervalo = Horizontal(1, 100)