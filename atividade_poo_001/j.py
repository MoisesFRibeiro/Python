# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
import os


# Classe 
class Perimetro:
# Método Construtor
    def __init__(self, Base, Altura,):
        self.Base = Base
        self.Altura = Altura

    def perimetro(self):
        return (self.Base + self.Altura ) * 2
    
# Entrada de Dados pelo Usuário
Base = float(input('digite a sua base: '))
Altura = float(input('digite a altura: '))

print(f'o perimetro calculado foi: {Perimetro}')
    

    