import math
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        return f"Saldo: {self.saldo}"
