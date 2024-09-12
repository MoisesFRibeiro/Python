# Metodo da super classe com sobrecarga de metodo

class ClassePai: # super classe
    # método coinstrutor
    def __init__(self, a, b):
        self.a = a 
        self.b = b

    # metodo que vai ser sobrecarregado
    def metodo_classe(self):
        print('Aqui vou multiplicar a e b!')
        resultado = self.a + self.b
        print(f'Este cálculo está sendo realizado')
        print(f'pelo Métododa Classe Pai!')
        print(f'O resultado da saoma de {self.a} e {self.b} = {resultado}')


class ClasseFilha(ClassePai): # classe derivada
    # Métdodo construtor
    def __init__(self, a, b):
        super().__init__(a, b) # chama o construtor da classe pai 
        # Não é nescessario redefinir a variavel self.a e self.b.
        # pois ja fora inicializadas pelo construtor da classe pai
               
    # sobrecarga de metodo
    def metodo_classe(self):
        # primeiro execulta o metodo da classe pai
        super().metodo_classe()
        # Depois, execulta o metodo da classe filha
        resultado = self.a + self.b
        print(f' O resultado da soma na classe filha é: {resultado} ')


# programa principal
teste = ClasseFilha(1, 2) 
teste.metodo_classe()                  