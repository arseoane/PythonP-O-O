class Horas:
    def __init__(self, horas, minutos, segundos):
        if ((horas >= 0 and horas <= 24) and (minutos >= 0 and minutos <= 60) and (segundos >= 0 and segundos <= 60)) == True:
            self.horas = horas
            self.minutos = minutos
            self.segundos = segundos
        else:
            self.horas = 0
            self.minutos = 0
            self.segundos = 0


    def getSegundos(self):
        return self.segundos

    def getMinutos(self):
        return self.minutos

    def getHoras(self):
        return self.horas

    def setSegundos(self, segundos):
        self.segundos = segundos

    def setMinutos(self, minutos):
        self.minutos = minutos

    def setHoras(self, horas):
        self.horas = horas

    def converterSegundos(self, segundos):
        return segundos / 3600

    def converterMinutos(self, minutos):
        return minutos / 60

    def incrementarSegundos(self, segundos):
        self.segundos += segundos

    def incrementarMinutos(self, minutos):
        self.minutos += minutos

    def incrementarHoras(self, horas):
        self.horas += horas

    def mostrarFormato12Horas(self):
        if self.horas > 12:
            return f"{(self.horas - 12):02d}:{self.minutos:02d}:{self.segundos:02d} PM"
        else:
            return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d} AM"