# Faça um programa que imprima os números no intervalo
# entre 1 e 10 em ordem inversa.
import os 


# Classe
class Inversão: # Classe pai
    # Método construtor
    def __init__(self, Inicial, Final,):
        self.Inicial = Inicial
        self.Final = Final
        
     # Método para realizar o intervalo na ordem inversa
        for var in range(Inicial, Final):
            # sobrecarregar  na classe filha
            pass

    #  Classe filha
class Ordem(Inversão):
    # Herda todos os atributos da classe pai podendo ter outros atributos 
    def  __init__(self, Inicial, Final, Ordem):
         self.Inicial = Inicial
         self.Final = Final

         # Herança da classe pai
         for var in range(Inicial, Final):
            return print(f'ordem [::-1]')
            

    # Instanciando o objeto Inicial, Final
    Inicial = [1]
    Final = [10]
    
    print(f'ordem [::-1]')