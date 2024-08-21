import os


class veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


# solicitando entrada de dados do usuário        
os.system('cls')
print('-'*70)
marca = input('digite a marca do veiculo: ')
modelo = input('digite o modelo do veiculo: ')
ano = input('digite o ano do veiculo: ')
cor = input('digite a cor do veiculo: ')

# cirando um objeto da classe veiculo com os dados fornecidos pelo usuário
veiculo1 = veiculo(marca, modelo, ano, cor)

# acessando e imprimindo atributos do objeto
print('-'*70)
print('\nInformações do veiculo: ')
print('='*70)
print(f'marca: {veiculo1.marca}')
print(f'modelo: {veiculo1.modelo}')
print(f'ano: {veiculo1.ano}')
print(f'cor: {veiculo1.cor}')
print('-'*70) 