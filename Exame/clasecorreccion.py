class Persona:
    def __init__(self, nombre, dni, nuss, telefono):
        self.__nombre = ""
        self.__dni = "0"
        self.__nuss = "00/00000000/00"
        self.__telefono = "+00 000 000 000"

        self.nombre = nombre
        self.dni = dni
        self.nuss = nuss
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor != "":
            self.__nombre = valor
        else:
            self.__nombre = ""

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if valor != "":
            self.__dni = valor
        else:
            self.__dni = "0"

    @property
    def nuss(self):
        return self.__nuss

    @nuss.setter
    def nuss(self, valor):
        partes = valor.split("/")
        if len(partes) == 3 and partes[0].isdigit() and len(partes[0]) == 2 and \
           partes[1].isdigit() and len(partes[1]) == 8 and \
           partes[2].isdigit() and len(partes[2]) == 2:
            self.__nuss = valor
        else:
            self.__nuss = "00/00000000/00"

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if len(valor) == 16 and valor[0] == '+' and valor[1:3].isdigit() and \
           valor[3] == ' ' and valor[4:7].isdigit() and \
           valor[7] == ' ' and valor[8:11].isdigit() and \
           valor[11] == ' ' and valor[12:15].isdigit():
            self.__telefono = valor
        else:
            self.__telefono = "+00 000 000 000"

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.dni == other.dni
        return False

