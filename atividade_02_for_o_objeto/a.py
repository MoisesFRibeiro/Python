# Faça um programa que imprima os números no intervalo entre 1 e 100.
#  Os números devem ser apresentados na horizontal.
import os 


# classe
class Numeros:
    # Método construtor
    def __init__(self, Inicial, Final):
        self.Inicial = Inicial
        self.Final = Final

# Método da classe para determinar intervalo 
    def determinar_intervalo(self):
        # sobrecarregar na classe filha
        pass

# Classe filha
        class Imprimir_intervalo(Numeros):
# Herdando todos os atributos da classe pai podendo ter outros atributos
            def __init__(self, Inicial, Final):
                self.Inicial = Inicial
                self.Final = Final

# Herança da classe pai
        def determinar_intervalo(self):
            for var in range(self.Inicial, self.Final+1):
                print(f'{var}', end=" | ")

        
# Instancia objeto intervalo
        intervalo = Imprimir_intervalo(1, 100)

# Saida de dados
        print('-'*70)
        print(f' NUMEROS ENTRW {intervalo.Inicial} e {intervalo.Final}')
        print('-'*70)
        intervalo.determinar_intervalo() # chamando o método determinar intervalo
        print()