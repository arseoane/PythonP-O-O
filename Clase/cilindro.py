import math
class Cilindro:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def propiedades_cilindro(r:float, h:float):
        areabase = math.pi * r ** 2
        arealat = 2 * math.pi * r * h
        areatotal = 2 * math.pi * r * (r + h)
        volume = math.pi * r ** 2 * h
        resultados = {
            "Área base = ": areabase,
            "Área lateral = ": arealat,
            "Área total = ": areatotal,
            "Volume = ": volume
        }
        resultado = ""
        for key, value in resultados.items():
            resultado += key + " " + str(value) + "\n"
        return resultado