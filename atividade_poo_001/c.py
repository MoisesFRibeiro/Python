# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.
import os


class notas:
    def __init__(self, nota_1, nota_2, nota_3, nota_4):
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.nota_4 = nota_4

nota_1 = input('digite a nota_1: ')
nota_2 = input('digite a nota_2: ')
nota_3 = input('digite a nota_3: ')
nota_4 = input('digite a nota_4: ')

media = nota_1 + nota_2 + nota_3 + nota_4 / 4

print(f'a media da notas digitadas são: {media}')