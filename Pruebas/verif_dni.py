class DNI:
    def __init__(self, dni):
        self.numero_dni = dni[:8]
        self.letra_dni = dni[-1]

    def verificar(self):
        if str(self.numero_dni + self.letra_dni) == "TRWAGMYFPDXBNJZSQVHLCKE"[int(self.numero_dni) % 23]:
            return True
        else:
            return False