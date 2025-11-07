import math
class Esfera:
    def __init__(self, r):
        self.r = r

    def propiedades_esfera(r):
        area = 4 * math.pi * (r ** 2)
        diametro = 2 * r
        volume = (4/3) * math.pi * (r ** 3)
        resultado = f"Área = {area}\nDiámetro = {diametro}\nVolume = {volume}"
        return resultado