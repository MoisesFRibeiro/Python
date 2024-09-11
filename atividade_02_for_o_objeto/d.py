# Faça um programa que imprima os números pares entre 0 e 100.
import os


# Classe
class Pares: # Classe pai
    # Método construtor
    def __init__(self, numeros_pares,):
        self.numeros_pares = numeros_pares
        
        def Imprimir_Pares(self):
            # sobrecarregar na classe filha
            pass

# Classe filha
        class Imprimir(Pares):
            def __init__(self, numeros_pares,):
                self.numeros_pares = numeros_pares

# Herança da classe pai
        Imprimir = Imprimir_Pares

    # Instanciando numeros pares
    numeros_pares = (0, 100)

    #  Método para realizar a contagem de numeros pares
    for var in range(0, 100):
        numeros_pares = numeros_pares
        if(numeros_pares % 2 == 0):
            print(f'os numeros primos pares são: {numeros_pares} ')  
            