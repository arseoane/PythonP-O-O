class Libro:
    def __init__(self, titulo, autor, ano, numPags, valor):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.numPags = numPags
        self.valor = valor

    def amosarLibro(self):
        return f'''Título: {self.titulo}
Autor: {self.autor}
Ano: {self.ano}
Núm. Pags: {self.numPags}
Valoración: {self.valor}'''

class Coche:
    def __init__(self):
        self.velocidade = 0

    def getVelocidade(self):
        return f"Velocidade: {self.velocidade} km/h"

    def acelerar(self, suma):
        self.velocidade += suma

    def frenar(self, resta):
        self.velocidade -= resta

class Conta:
    def __init__(self, nome, numconta, tipointerese, saldo):
        self.nome = nome
        self.numconta = numconta
        self.tipointerese = tipointerese
        self.saldo = saldo

    @property
    def nome(self):
        return self.nome

    def ingreso(self, valor):
        self.saldo += valor

    def info(self):
        return f'''Nome: {self.nome}\nNúmero de conta: {self.numconta}\nTipo de interese: {self.tipointerese}\nSaldo: {self.saldo}'''