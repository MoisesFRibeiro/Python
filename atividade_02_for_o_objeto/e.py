# Faça um programa que some a quantidade de números pares
# encontrados no intervalo entre 0 e 100.
import os


# Classe
class Pares: # Classe pai
    # Método construtor
    def __init__(self, pares, intervalo,):
        self.pares = self.encontrar_pares()
        self.intervalo = intervalo

        #  Método da classe para encontrar a quantidade de numeros pares
        def Quantidade(self):
              self.pares =  self.Encontar_pares()
              self.intervalo = intervalo
              return len(self.pares)
        # sobrecarregar na classe filha
        pass

# Classe filha
class Intervalo(Pares):
    # Herda todos os atributos da classe pai podendo ter outros atributos
    Intervalo = ()
    def Quantidade(self): # Método para encontrar a quantidade de numeros pares
          self.pares = self.Encontar_pares
          self.intervalo = Intervalo
          return len(self.pares)

# Método para encontrar todos os numeros pares dentro do intervalo
    def Encontar_pares(self):
            return[num for num in range(self.intervalo[0], self.intervalo[1] +1) if num % 2 == 0]
        

# Retornando um string formatada com a quantidade de numeros encontrados
    def __str__(self):
            return f'A quanidade de numeros pares encontrados foi{self.Quantidade()}

            # Instanciando intervalo
            intervalo = (0, 100)
            pares = Pares(Intervalo)

# Saida
print(f'{Intervalo}')