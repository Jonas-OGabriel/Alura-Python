

class Conta:

    def __init__(self, numero_conta, titular_conta, saldo_atual, limite_credito):
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

    def sacar(self, valor_saque):
        print("Sacando {} do saldo".format(valor_saque))
        self.__saldo -= valor_saque
        print("Extrato:")
        Conta.extrato(self)

    def transferir(self, valor_tranferencia, conta_destino):
        self.sacar(valor_tranferencia)
        conta_destino.depositar(valor_tranferencia)
    
    def get_saldo(self):
        return self.get_saldo
    
    @property
    def limite(self):
        return self.__limite

    def get_titular(self):
        return self.get_titular

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite