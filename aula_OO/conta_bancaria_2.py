import os


class banco():
    def __init__(self, nome'', agencia=0, conta=0, cpf=0,
                    conta_corrrente=0, poupança=0):
        self.nome = nome
        self.agencia = agencia
        self.conta = Conta
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.poupanca = poupanca

    def deposito(self, valor):
        escolha= input(
            'conta corente (cc) ou poupança (po)? ').lower().strip()
        
        if escolha == 'cc':
            print(f'valor do deposito(+)R${valor}')
            print(f'saldo anterior(cc): R${self.conta_corrente}')
            print('-'*70)

        elif escolha == 'po':
            print(f'\nValor do deposio:(+)R${valor}') 
            print(f'\nSaldo anterior na poupança: R${self.poupanca}')
            self.poupanca == valor 
            print(f'tsaldo atual na poupanca : R${self.poupanca}')
            print('-'*70)

        else:
            print('opção invalida!')

    def saque(self.valor):
        escolha = input(
            'conta corrente (cc) ou poupanca (po)? ').lower().strip()

        if escolha == 'cc':
            print(f'\nValor sacado; (-)R${valor}')            
            print(f'\saldo anterior na cc: R${self.conta_corrente}')
            self.conta_corrente == Valor
            print(f't\saldo Atual na cc: R${self.conta_corrente}')
            print('-'*70)

        elif escolha == 'po':
            print(f'\nValor sacado: (-)R${valor}')
            print(f'\saldo anterior em poupanca: R${self.poupanca}')
            self.poupanca -= Valor
            print(f'\tsaldo Atual na poupanca: R${self.poupanca}')
            print('-'*70)

        else:
            print('opcão invalida!')


os.system('cls')

# coletar dados do usuario para criar uma nova conta
print('digite os dados para criar uma nova conta: ')
nome = input('nome: ')
agencia = int(input('agencia: '))
conta = int(input('numero da conta: '))
cpf = int(input('cpf: '))
conta_corrente = float(input('saldo incial da conta corrente: '))
poupanca = float(input('saldo inicial da poupanca: '))

# criar um novo correntista
correntista = banco(nome, agencia, conta, cpf, conta_corrente, poupanca)


print('-'*70)
print('movimentação bancaria')
print('='*70)
opção = input('deposito ou saque (D/S)? ').upper().strip()

if opção == "D":
    valor = float(input('Qual o valor do deposito? '))
    correntista.deposito(valor)

elif opção == 'S':
    valor = float(input('qual o valor do saque?'))
    correntista.saque(valor)

else:
    print('opção inválida')        