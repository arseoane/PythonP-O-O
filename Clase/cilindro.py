import math
class Cilindro:
    def __init__(self, r):
        self.r = r

    def propiedades_cilindro(r, h, rho=None):
        Ab = math.pi * r ** 2
        Al = 2 * math.pi * r * h
        At = 2 * math.pi * r * (r + h)
        V = math.pi * r ** 2 * h
        resultado = {
            "Ab": Ab,
            "Al": Al,
            "At": At,
            "V": V
        }
        if rho is not None:
            m = rho * V
            Iz = 0.5 * m * r ** 2
            Ix = (1 / 12) * m * (3 * r ** 2 + h ** 2)
            resultado.update({
                "m": m,
                "Iz": Iz,
                "Ix": Ix,
                "Iy": Ix,
                "z_cm": h / 2
            })
        return resultado