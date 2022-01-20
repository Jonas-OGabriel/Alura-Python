

class Conta:

    def __init__(self, numero_conta = 0, titular_conta = "Teste", saldo_atual = 100.0, limite_credito = 1000.0):
        print("Contruindo objeto... {}".format(self))
        self.__numero = numero_conta
        self.__titular = titular_conta
        self.__saldo = saldo_atual
        self.__limite = limite_credito


    def extrato(self):
        print("Saldo: {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor_deposito):
        print("Depositando {} do saldo".format(valor_deposito))
        self.__saldo += valor_deposito
        print("Extrato:")
        self.extrato()

    def __pode_sacar(self, valor_saque):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel_para_saque

    def sacar(self, valor_saque):
        print("Sacando {} do saldo".format(valor_saque))
        if(self.__pode_sacar(valor_saque)):
            self.__saldo -= valor_saque
            print("Extrato:")
            Conta.extrato(self)
        else:
            print("Limite insuficiente para saque")

    def transferir(self, valor_tranferencia, conta_destino):
        self.sacar(valor_tranferencia)
        conta_destino.depositar(valor_tranferencia)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}