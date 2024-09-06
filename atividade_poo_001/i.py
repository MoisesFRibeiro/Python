# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.
import os 


# Classe
class Dolar:
    # Método Construtor
    def __init__(self, Reais, Dolares,):
        self.Reais = Reais
        self.Dolares = Dolares

    def Cotação_Dolar(self):
             return self.Reais / self.Dolares
    
# Entrada de Dados
Reais = float(input('entre com valor em Reais: R$'))
Dolares = float(input('entre com valores em Dolares: U$$ '))

# Instancia apartir da Classe Dolar
conversão_dolar = Convercao(Reais, Dolar)
converter = conversão_dolar.para_dolar()

print(f'com R${Reais:2f} compramos{converter:.2f} dólares')