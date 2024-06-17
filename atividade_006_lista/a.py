# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.
import os


os.system('cls')

print('-'*70)
print('criando lista')
print("-"*70)

lista_numeros = [1, 2, 3, 5, 6]
lista_numeros.insert()
for i in range(1):
    numero = int(input('digite o numero: ')) 

numero_verfificar = int(input('digite o numero: '))

if numero_verfificar in lista_numeros:
    print(f'o numero {numero_verfificar} esta na lista')
else:
    print(f'o numero {numero_verfificar} não esta na lista')    