class calcular_letra_dni:
    def __init__(self, numero_dni):
        self.numero_dni = numero_dni

    def letra_dni(numero_dni):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = letras[numero_dni % 23]
        return letra

