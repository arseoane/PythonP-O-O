class Horas:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas + (minutos/60) + (segundos/3600)
        self.minutos = minutos + (segundos/60)
        self.segundos = segundos