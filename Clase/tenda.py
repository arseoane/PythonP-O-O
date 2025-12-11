class Produto:
    def __init__(self, nome, prezo, cantidade, stock):
        self.nome = nome
        self.prezo = prezo
        self.cantidade = cantidade
        self.stock = stock

    def engadirPedido(self,cant):
        self.cantidade = cant

    def incrementarStock(self,cant):
        self.stock += cant

class Cliente:
    def __init__(self, nome, email, direccion, cpf):
        self.nome = nome
        self.email = email
        self.direccion = direccion

class Pedido:
    def __init__(self, listaprods, cliente, data):
        self.listaprods = listaprods
        self.cliente = cliente
        self.data = data

    def engadirProduto(self, produtor):
        self.listaprods.append(produtor)

    def eliminarProduto(self, produtor):
        self.listaprods.remove(produtor)

    def calculoPrezoTotal(self):
        total = 0
        for produtor in self.listaprods:
            total += produtor.prezo
        return total

    def calculoIVA(self):
        total = 0
        for produtor in self.listaprods:
            total += produtor.stock
        return total