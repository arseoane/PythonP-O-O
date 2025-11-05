class validar_dni():

    def __init__(self, dni):
        self.dni = dni

    def validar(dni):
        if str(dni)[:8].isnumeric() and str(dni)[-1].isalpha():
            return True
        else:
            return False