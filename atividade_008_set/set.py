# Trabalho de estrutura de dados SET
# Senac Minas Gerais/ Juiz de Fora
# Aluno: Moises De Souza Ribeiro
# Turma: 0152
# Ano: 2024
# Excluindo material escolar de uma lista 
     
import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: SET')
print('='*70)

# declarando lista de materiais
materiais_escolar = ["caneta", "lapis", "papel", "borracha"]
excluir = []

while True:

    excluir = input('selecione qual material deseja excluir( ou digite "s" para sair): ')

    if excluir.lower():
     materiais_escolar.remove('')

    elif (excluir != s):
       print('continue digitando......')
    
        
    print(f'a lista de materiais final foi:{materiais_escolar} ')
