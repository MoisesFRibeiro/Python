# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 05/08/2024
# convertendo graus

 import os 


 os.system('cls')

 print('-'*70)
 print('convertendo fahrenheit para celsius')
 print('='*70)

 def converter_graus():  
    temperatura_convertida = (temperatura - 32) * 5/9

    return temperatura_convertida


temperatura = float(input('Entre com a temperatura em Fahrenheit: '))

convertendo = converter_graus() 
print(f'A temperatura {temperatura} °F é igual a {convertendo:.2f} °C')
print()