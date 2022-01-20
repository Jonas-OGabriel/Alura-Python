

class Conta:

    def __init__(self, numero_conta, titular_conta, saldo_atual, limite_credito):
        print("Contruindo objeto... {}".format(self))
        self.numero = numero_conta
        self.titular = titular_conta
        self.saldo = saldo_atual
        self.limite = limite_credito