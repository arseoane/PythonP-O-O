class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info_basica(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, ano, velocidad=0,combustible=50):
        super().__init__(marca,modelo,ano)
        self.__encendido = False
        self.__velocidad = velocidad
        self.__combustible = combustible

    def encender(self):
        self.__encendido = True
        print("El coche está encendido.")

    def apagar(self):
        self.__encendido = False
        print("El coche está apagado.")

    def acelerar(self, incremento):
        if self.__combustible <= 0:
            print("¡Combustible agotado!")
        else:
            self.__velocidad += incremento
            print(f"Acelerando... Velocidad actual: {self.__velocidad} km/h")
            self.__combustible -= incremento

    def frenar(self, decremento):
        self.__velocidad -= decremento
        print(f"Frenando... Velocidad actual: {self.__velocidad} km/h")

    def repostar(self, litros):
        self.__combustible += litros
        print(f"Repostando... Combustible actual: {self.__combustible} litros")

    def info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}")
        if (self.__encendido == False):
            print("Estado: Apagado")
        else:
            print("Estado: Encendido")
        print(f"Velocidad: {self.__velocidad} km/h\nCombustible: {self.__combustible} litros")

    @property
    def leerVel(self):
        return str(self.__velocidad)

class Moto(Vehiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def hacer_caballito(self):
        print("¡Wheeee! Haciendo caballito 🏍️")

    def info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}\nCilindrada: {self.cilindrada}cc")

class Camion(Vehiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca,modelo,ano)
        self.carga_maxima = carga_maxima
        self.carga_actual = 0

    def cargar(self, kg):
        self.carga_actual += kg
        if self.carga_maxima < self.carga_actual:
            print("¡Carga máxima excedida!")
        else:
            print(f"Cargando... Carga actual: {self.carga_actual} kg")

    def info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}\nCarga máxima: {self.carga_maxima} kg\nCarga actual: {self.carga_actual} kg")