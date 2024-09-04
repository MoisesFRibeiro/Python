# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
import os


class nascimento:
    def __init__(self, nascimento):
        self.nascimento = nascimento
        
# solicitando entrada de dados
nascimento = input('digite o ano de nascimento: ')

from datetime import date
data_atual = date.today()
data_atual = data_atual.year
idade = data_atual-nascimento

print(f'a idade atual é {idade}')