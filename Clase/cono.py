import math
class Cono:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def propiedades_cono(r:float, h:float):
        g = math.sqrt((r ** 2) * (h ** 2))
        diametro = 2 * r
        areabase = math.pi * (r ** 2)
        arealateral = math.pi * r * g
        areatotal = math.pi * r * (g + r)
        volumen = (1/3) * math.pi * (r ** 2) * h

        return f"Diámetro: {diametro}\nÁrea base: {areabase}\nÁrea lateral: {arealateral}\nÁrea total: {areatotal}\nVolumen: {volumen}"
