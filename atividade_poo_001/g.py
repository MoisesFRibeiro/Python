# Faça um programa que converta metros em centímetros e milímetros.
import os 


# Classe 
class conversor:
    # Método construtor
    def __init__(self, Metros, Centimetros, Milimetros):
        self.Metros = Metros
        self.Centimetros = Centimetros
        self.Milimetros = Milimetros

# Entrada de Dados
Metros = input('digite quantos Metros: ')

# Convertendo para float
Metros_float = float

# Conventendo Metros em Centimetros e Milimetros
Centimetros = (Metros * 100)
Milimetros = (Metros * 1000)

print(f'o resultado da conversão em centimetros: {Centimetros} e em milimetros {Milimetros}')