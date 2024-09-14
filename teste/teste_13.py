import os


# classe pai
class Banda:
    # Método construtor
    def __init__(self, aerosmith):
        self.aerosmith = aerosmith

    # metodo para ser utilizado na classe filha
    def Tocar(self):
        pass
     
class Rock(Banda): # classe filha
    def Tocar(self):
            return aerosmith
    
    # Instanciando objeto tocar
aerosmith = Banda
aerosmith.Rock