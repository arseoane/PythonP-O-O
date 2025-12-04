class Horas:
    coleccionHoras = []
    coleccionMinutos = []
    coleccionSegundos = []

    def __init__(self, horas, minutos, segundos):
        if ((horas >= 0 and horas <= 24) and (minutos >= 0 and minutos <= 60) and (segundos >= 0 and segundos <= 60)) == True:
            self.horas = horas
            self.minutos = minutos
            self.segundos = segundos
        else:
            self.horas = 0
            self.minutos = 0
            self.segundos = 0
        self.__class__.coleccionHoras.append(self.horas)
        self.__class__.coleccionMinutos.append(self.minutos)
        self.__class__.coleccionSegundos.append(self.segundos)


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

    def __asignacionHoraColeccion(self, horas):
        if len(str(horas)) >= 3:
            if isinstance(str(horas)[2], int):
                Horas.coleccionHoras.append(int(str(horas)[0]))
            else:
                Horas.coleccionHoras.append(0)

    def __asignacionMinutoColeccion(self, minutos):
        if len(str(minutos)) >= 3:
            if isinstance(str(minutos)[2], int):
                Horas.coleccionMinutos.append(int(str(minutos)[0]))
            else:
                Horas.coleccionMinutos.append(0)

    def __asignacionSegundoColeccion(self, segundos):
        if len(str(segundos)) >= 3:
            if isinstance(str(segundos)[2], int):
                Horas.coleccionSegundos.append(int(str(segundos)[0]))
            else:
                Horas.coleccionSegundos.append(0)

    def mostrarHoras(self):
        return Horas.coleccionHoras

    def mostrarMinutos(self):
        return Horas.coleccionMinutos

    def mostrarSegundos(self):
        return Horas.coleccionSegundos