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
        if self.horas > 12 and self.horas <= 24:
            return f"{(self.horas - 12):02d}:{self.minutos:02d}:{self.segundos:02d} PM"
        elif self.horas > 24:
            return f"00:00:00 XX"
        else:
            return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d} AM"

    def __asignacionHoraColeccion(self,horas):
        if len(horas) == 3:
            if isinstance(horas[3], int):
                self.setHoras(horas[0])
            else:
                self.setHoras(0)

    def __asignacionMinutoColeccion(self,minutos):
        if len(minutos) == 3:
            if isinstance(minutos[3], int):
                self.setMinutos(minutos[0])
            else:
                self.setMinutos(0)

    def __asignacionSegundoColeccion(self,segundos):
        if len(segundos) == 3:
            if isinstance(segundos[3], int):
                self.setSegundos(segundos[0])
            else:
                self.setSegundos(0)
