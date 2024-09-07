# Faça um programa que imprima os números no intervalo
# entre 1 e 10 em ordem inversa.
import os 


# Classe
class Inversão:
    def __init__(self, Inicial, Final, Ordem):
        self.Inicial = Inicial
        self.Final = Final
        self.Ordem = Ordem

    # Entrada de dados
    Inicial = [1]
    Final = [10]
    
    for var in range(Inicial, Final):
        print(f'ordem [::-1]')