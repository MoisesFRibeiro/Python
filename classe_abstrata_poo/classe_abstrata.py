import os
from abc import ABC, abstractmethod

#  Classe abstrata
class MetodoDePagamento(ABC):

    @abstractmethod
    def processar_pagamento(self, valor):
        # Processa um pagamento qualquer
        pass

# subclasse concreta
class CartaoDeCredito(MetodoDePagamento):

    def processar_pagamento(self, valor):
        print(f'Pagamento com  cartão de crédito.')
        print(f'valor pago: R${valor}')

# Subclasse concreta
class Boleto(MetodoDePagamento):

    def processar_pagamento(self, valor):
        print('Emissão de Boleto')
        print(f"pagamento de R${valor}.")

os.system('cls')
# Instanciando as classes filhas
pagamento_cartao = CartaoDeCredito()
pagamento_cartao.processar_pagamento(5000.00)

pagamento_boleto = Boleto()
pagamento_boleto.processar_pagamento(500.00)