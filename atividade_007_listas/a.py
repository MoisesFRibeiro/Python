# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# Mostre a quantidade de notas que foram lidas.
# Exiba todas as notas na ordem em que foram informadas.
# Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# Calcule e mostre a soma das notas.
# Calcule e mostre a média das notas.
import os


os.system('cls')

notas = []
for i in range(0,5):
    valor = int(input('digite a nota: '))
    if (valor < 0):
        print('fim')