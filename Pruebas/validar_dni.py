class validar_dni():

    def __init__(self, dni):
        self.dni = dni

    def validar(dni):
        if str(dni)[:8].isnumeric() and str(dni)[-1].isalpha() and str(dni)[-1].isupper and len(str(dni)) == 9:
            return dni
        else:
            return ""