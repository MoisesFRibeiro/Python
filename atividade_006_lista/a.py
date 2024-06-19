# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.
import os


os.system('cls')

lista_numeros = [1, 2, 3, 5, 6]
posição = int(input('posição onde deseja o elemento: '))
elemento = input('elemento a ser inserido: ')

if posição >= 0 and posição <= len(lista_numeros):
    lista_numeros.insert(posição, elemento)
    print('lista após inserção', lista_numeros)
else:
    print((f'a posição fora do intervalo 0,{len(lista_numeros)} '))    