import math

class Cono:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def generatriz(radio, altura):
        return math.sqrt(radio**2 + altura**2)

    def superficie_lateral(radio, altura):
        return math.pi * radio * (math.sqrt(radio**2 + altura**2))

    def superficie_total(radio, altura):
        return (math.pi * radio * (math.sqrt(radio**2 + altura**2))) + math.pi * radio**2

    def volumen(radio, altura):
        return (1/3) * math.pi * radio**3 * (altura / radio)
