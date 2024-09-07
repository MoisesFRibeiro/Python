# Evolua o programa anterior para um código que pergunte ao usuário
# qual o intervalo que ele deseja ver  impresso.
import os


# Classe
class Horizontal:
    # Método Construtor
    def __init__(self, Numero_inicial, Numero_Final):
        self.Numero_inicial = Numero_inicial
        self.Numero_final = Numero_Final
        
    def intervalo(self):
        return
    
    # Entrada de dados pelo usuário
    Numero_inicial = int(input('entre com o número inicial: '))
    Numero_final = int(input('entre com o número final:'))
     
    # Método para realizar contagem
    for var in range(self.inicial, self.final + 1):
        print(f'{var}' , end=" | " )

    # Criando uma instância
    intervalo = Horizontal(1, 100)       
    Horizontal = (Numero_inicial, Numero_final)