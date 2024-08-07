# Crie uma função que receba uma lista de números. 
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.

import os


os.system('cls')

# definindo uma função para numeros
def pegar_par_impar(lista):
    pares = []
    impares = []

    print(f'lista: {lista}')
    for i in lista:
        if (i % 2 == 0):
            pares.append(i)

        else:
            impares.append(i)

    print(f'a lista possui{len(pares)} numeros pares')
    print(f' lista pares: {pares}')
    print()
    print(f'lista possui{len(impares)} numeros impares')
    print(f'lista impares: {impares}')

    return pares

lista = [1, 2, 3, 4, 5, 6,]

pegar_par_impar(lista)

