# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.
import os

# Classe
class Casas_decimais:
    def __init__(self, crianças, balas):
        self.crianças = crianças
        self.balas = balas

    def Dividir_Balas(self):

# convertendo para float para permitir diviões decimais
        crianças_float = float(self.crianças)
        balas_float = float(self.balas)

# verificando se o numero de crianças é diferente de zero        
        if crianças_float == 0:
            raise ValueError(" o numero de crianças não pode ser 0.")

        balas_por_criança = balas_float / crianças_float


# Saida Formatada com 4 Casas Decimais
        print(f'a quantidade de balas por crianças{round(balas_por_criança, 4)}')