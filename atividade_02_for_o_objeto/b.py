# Evolua o programa anterior para um código que pergunte ao usuário
# qual o intervalo que ele deseja ver  impresso.
import os


# Classe
class Numeros:# Classe pai
    # Método Construtor
    def __init__(self, Numero_inicial, Numero_Final):
        self.Numero_inicial = Numero_inicial
        self.Numero_final = Numero_Final

 # Método para determinar intervalo numérico
    def derterminar_intervalo(self):
        #sobrecarregar na classe filha
            pass
       
 # Classe filha
            class ImprimirIntervalo(Numeros):
                 # Herda todos os atributos da classe pai podendo ter outros atributos
                 def __init__(self, Numero_inicial, Numero_Final):
                        self.Numero_inicial = Numero_inicial
                        self.Numero_final = Numero_Final

 # Herança da classe pai
    def derterminar_intervalo(self):
        for var in range(self.numero_inicial, self.numero_final+1):# Realizando a contagem
            print(f'{var}', end=" | ")

           
    # Entrada de dados pelo usuário
    Numero_inicial = int(input('entre com o número inicial: '))
    Numero_final = int(input('entre com o número final:'))
     
    # Criando uma instância
    intervalo = ImprimirIntervalo()
    
    print('-'*70)
    print(f'Numeros entre {intervalo.Numero_inicial} e {intervalo.Numero_final}')
    print('-'*70)
    intervalo.determinar_intervalo() # chamando o método determinar intervalo
    print()