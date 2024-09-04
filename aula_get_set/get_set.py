import os
import math


class equacao:
    def __init__(self, a=1, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    # getters    
    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def get_c(self):
        return self._c
    
    # setters
    def set_a(self, value):
        self._a = value

    def set_b(self, value):
        self._b = value

    def set_c(self, value):
        self._c = value

    def calcular_raizes(self):

        # calculando o delta
        delta = self._b ** 2 -4 * self._a * self._c

        if delta < 0:
            return 'a equação não possui raizes reais.'
        elif delta == 0:
            raiz = -self._b / (2 * self._a)
            return f'a equação possui uma raiz real: {raiz}'
        else:
            x1 = (-self._b + math.sqrt(delta)) / (2 * self._a)
            x2 = (-self._b - math.sqrt(delta)) / (2 * self._a)
            return f'a equação possui duas raizes reais: {x1} e {x2}'
        

os.system('cls')
print('-'*70)
print('calcculo da equação de 2* grau')
print('-'*70)
equacao1-- equacao(1, -3, 2)
print(equacao.)