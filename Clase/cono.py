import math

class Cono:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def generatriz(self):
        return math.sqrt(self.radio**2 + self.altura**2)

    def superficie_lateral(self):
        return math.pi * self.radio * self.generatriz()

    def superficie_total(self):
        return self.superficie_lateral() + math.pi * self.radio**2

    def volumen(self):
        return (1/3) * math.pi * self.radio**3 * (self.altura / self.radio)
