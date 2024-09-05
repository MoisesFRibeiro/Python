# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
import os


# Classe
class Numero:
    # Método construtor
    def __init__(self, Número, Dobro, Triplo):
        self.Número = Número
        self.Dobro = Dobro
        self.Triplo = Triplo

# Entrada de dados
Número = input('entre com o numero: ')    
 
# Método para calcular o dobro e o triplo
Dobro = Número * 2 
Triplo = Número * 3 

print(f'o dobro do numero é: {Dobro}, e o triplo do numero é: {Triplo}')