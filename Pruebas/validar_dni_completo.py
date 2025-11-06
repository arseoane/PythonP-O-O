class validar:

    def __init__(self, dni):
        self.dni = dni

    def validar(dni):
        if len(dni) == 9 and dni[:8].isnumeric() and dni[-1].isupper():
            return dni
        else:
            return "00000000X"