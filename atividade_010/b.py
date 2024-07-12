# Crie uma função que cadastre o nome de uma aluno, a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for. 

import os 


os.system('cls')

aluno = []
nome = []

# definindo a funçaõ cadastrar aluno
def cadastrar_aluno(nome, matricula, Dt_nascimento):

nome = str(input('entre com o nome do aluno: '))
matricula = input('entre com a matricula do aluno: ')
nascimento = input('entre com o nascimento do aluno: ')


print(f'o nome do aluno cadastrado é: {nome}')
print(f'a matricula do aluno é: {matricula}')
print(f'o nascimento do aluno é: {nascimento}')