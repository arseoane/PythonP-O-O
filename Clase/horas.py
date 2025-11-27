class Horas:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def setHoras(self, horas):
        self.horas = horas

    def setMinutos(self, minutos):
        self.minutos = minutos

    def setSegundos(self, segundos):
        self.segundos = segundos

    def getHoras(self):
        return self.horas

    def getMinutos(self):
        return self.minutos

    def getSegundos(self):
        return self.segundos

    def converterSegundos(self):
        return self.segundos/3600

    def converterMinutos(self):
        return self.minutos/60

    def incrementHoras(self, horamas):
        self.horas += horamas

    def incrementMinutos(self, minmas):
        self.minutos += minmas

    def incrementSegundos(self, segmas):
        self.segundos += segmas
