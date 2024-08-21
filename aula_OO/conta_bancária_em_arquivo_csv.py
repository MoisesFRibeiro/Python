import csv
import os


class conta_bancaria:
    def __init__(self, numero-conta, nome_titular, saldo, agencia, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        
# função para obter os dados do usuário  e criar uma instância da conta bancaria
def obter_dados_conta():
    numero_conta = input('digite o numero da conta: ')
    nome_titular = input('digite o nome do titular: ')
    saldo = float(input('digite o saldo inicial: '))
    agencia = input('digite a agencia: ')
    tipo_conta = input('digite o tipo de conta: ')
    return conta_bancaria(numero_conta, nome_titular, saldo, agencia, tipo_conta)

# lista para armazenar conta bancária:
contas = [] 

#obter dados da conta
while True:
    conta = obter_dados_conta()
    contas.append({
        'numero_conta': conta.numero_conta,
        'nome_titular': conta.nome_titular,
        'saldo': conta.saldo,
        'agencia': conta.agencia,
        'tipo_conta': conta.tipo_conta
    })
    continuar = input('deseja adicionar outra conta? (s/n): ')
    if continuar.lower() != 's':
        break

# caminhpo para a pasta onde o arquivo csv será salvo
pasta ='arquivo_csv/conta/'

# verificando se a pásta existe, se não ira cria-la
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo csv para gravar as informções
arquivo = 'arquivo_csv/conta/conta.csv' 

# escrevera lista de dicionÁRIOS NO ARQUIVO CSV
with open(arquivo, mode='w', newline='') as conta:
    