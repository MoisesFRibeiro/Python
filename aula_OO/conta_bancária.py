import os


class contabancaria:
    def __init__(self, numero_conta, nome_titular, saldo, agencia, tipo_conta): 
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta


# solicitando entrad de dados do usuário
print('-'*70)
os.system('cls')
numero_conta = input('digite o numeroda conta: ')
nome_titular = input('digite o nome do titular: ')
saldo = float(input('digite o saldo inicial: '))
agencia = input('digite a agencia: ')
tipo_conta = input('digite o tipo de conta: ')
