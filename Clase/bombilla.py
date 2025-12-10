class Bombilla:
    def __init__(self, onoff=False):
        if type(onoff) == bool:
            self.onoff = onoff
        else:
            self.onoff = False

    def encender(self):
        self.onoff = True

    def apagar(self):
        self.onoff = False

    def estado(self):
        if self.onoff:
            return "Encendido"
        else:
            return "Apagado"