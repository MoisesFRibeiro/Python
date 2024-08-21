import os


class pessoa:
    def __init__(self, nome, cpf, nascimento, cep, cidade, estado):
       # inicializando os atributos
       self.nome = nome
       self.cpf = cpf
       self.nascimento = nascimento
       self.cep = cep
       self.cidade = cidade
       self.estado = estado


# solicitando entrad do usuário
os.system('cls')
print('-'*70)
nome = input('digite o nome: ')
cpf = input('digite o cpf: ')
nascimento = input('digite o ano de nascimento: ')
cep = input('digite o cep: ')
cidade = input('digite a cidade: ')
estado = input('digite o estado: ')

# criando um objeto da classe com os dados fornecidos pelo usuario
pessoa1 = pessoa(nome, cpf, nascimento, cep, cidade, estado)

# acessando e imprimindo atributos do objeto
print('-'*70)
print('\nInformações da pessoa:')
print('='*70)
print(f'nome: {pessoa1.nome}')
print(f' cpf: {pessoa1.cpf}')
print(f'ano de nascimento: {pessoa1.nascimento}')
print(f'cep: {pessoa1.cep}')
print(f'cidade: {pessoa1.cidade}')
print(f'estado: {pessoa1.estado}')
print('-'*70)