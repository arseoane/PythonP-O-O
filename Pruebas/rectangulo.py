import math
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * self.ancho + self.alto

    def e_cadrado(self):
        return self.ancho == self.alto
