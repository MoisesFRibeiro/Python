import os


# Classe
class MinhacClasse:
# Método construtor
    def __init__(self, valor):
        self._atributo = valor

        @property
        def atributo(self):
            return self._atributo

        @atributo.setter
        def atributo(self, valor):
            self._atributo = valor
obj = MinhacClasse(10)
# o atributo trabalha como uma variavel
obj.atributo = 20 # (set)                
# saida semelhante a uma variavel
print(obj.atributo) # (get)