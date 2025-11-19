class Coche:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(marca,modelo,ano):
        return f"Marca: {marca}, modelo: {modelo}, ano: {ano}."