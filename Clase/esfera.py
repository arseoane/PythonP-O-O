import math

class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def diametro(radio):
        return radio * 2

    def superficie(radio):
        return 4 * math.pi * (radio ** 2)

    def volumen(radio):
        return (4/3) * math.pi * (radio ** 3)