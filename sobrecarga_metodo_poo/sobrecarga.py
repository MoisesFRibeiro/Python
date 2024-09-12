# Sobrecarga de Métodos

class Classepai: # Super Class
    # Método Construtor
    def __init__(self, a, b,):
        self.a = a
        self.b = b 

    # para sobrecarregar
    # vai ser usada para soma 2 números
    def metodo_classes(self, a, b):
        pass


class ClasseFilha: # classe derivada 
    # metodo construtor
    def __init__(self, a, b):
        self.a = a 
        self.b = b

        # sobrecarrega o metodo
    def metodo_classe(self):
            return self.a + self.b 


# programa principal
teste = ClasseFilha(1, 2)
teste.metdo_classe()
