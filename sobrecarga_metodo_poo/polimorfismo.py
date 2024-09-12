# polimorfismo

from math import pi

# Define a classe base forma com um metodo area
# que não faz nada (é quaase uam classe abstrata)


class Forma:
    def area(self):
        pass


# Define a classe circulo que herda de forma
# o construtor __init__ inicializa a 'raio'
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

        # Define o método para calcular a area do
        # circulo usado e formula  r* raio²
    def area(self):
        return pi * (self.raio ** 2)

# Define a classe retangulo que herda de forma
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # Define o metodo area para calcular a area
    # do retangulo usado a formula largura  * altura
    def area(self):
        return self.largura * self.altura


# Define a classe Quadrado que herda de Retangulo
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


# Define uma função exibir_area que aceita um
# Objeto forma e imprime sua area
# o metodo area é chamado no objeto forma
def exibir_area(forma):
    print(f'A area da forma é: {forma.area()}')


# Cria instancia e circula, Retangulo e Quadrado
circulo = Circulo(5)
retangulo = Retangulo(4, 6)
quadrado = Quadrado(3)

# Chama a função exibir_area para cada instancia
# O metodo  area apropriado é chamado para
# cada objeto, mostrando polimorfismo
exibir_area(circulo)
exibir_area(retangulo)
exibir_area(quadrado)
