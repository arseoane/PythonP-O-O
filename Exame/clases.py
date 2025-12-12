import datetime
from datetime import timedelta


class Persoa:
    def __init__(self, nome, dni, codpostal):
        self.nome = nome
        self.dni = dni
        if len(str(codpostal)) == 5:
            self.codpostal = codpostal
        else:
            self.codpostal = "00000"

    def comparar(self, persoaComp):
        if self.dni == persoaComp.dni:
            return True
        else:
            return False

    def __str__(self):
        return f"Nome: {self.nome}\nDNI: {self.dni}\nCódigo Postal: {self.codpostal}"

class ClienteTel:
    def __init__(self, nome, dni, codpostal, numtelefono):
        self.nome = nome
        if len(dni) == 9 and dni[-1].isalpha() and dni[:8].isnumeric():
            self.dni = dni
        else:
            self.dni = "00000000X"

        if len(str(codpostal)) == 5:
            self.codpostal = codpostal
        else:
            self.codpostal = "00000"

        if len(numtelefono) == 15 and numtelefono[0] == "+" and numtelefono[3] == " " and numtelefono[7] == " " and numtelefono[11] == " ":
            numtelsinesp = numtelefono.replace(" ", "")
            numtelsinesp = numtelsinesp.replace("+", "")
            if numtelsinesp.isdigit():
                self.numtelefono = numtelefono
        else:
            self.numtelefono = "+00 000 000 000"

    def __str__(self):
        return f"Nome: {self.nome}\nDNI: {self.dni}\nCódigo Postal: {self.codpostal}\nNúmero Telefono: {self.numtelefono}"

class Chamada:
    def __init__(self, cliente, interlocutor, data_hora_ini, data_hora_fin, sainte):
        self.cliente = cliente
        self.interlocutor = interlocutor
        if type(data_hora_ini) == datetime.datetime:
            self.data_hora_ini = data_hora_ini
        else:
            self.data_hora_ini = "XXXX-XX-XX XX:XX:XX.XXXXXX"

        if type(data_hora_fin) == datetime.datetime:
            self.data_hora_fin = data_hora_fin
        else:
            self.data_hora_fin = "XXXX-XX-XX XX:XX:XX.XXXXXX"

        self.sainte = sainte

    @property
    def minutosChamada(self):
        return ((max(self.data_hora_ini.hour,self.data_hora_fin.hour) - min(self.data_hora_ini.hour,self.data_hora_fin.hour)) * 60) + (max(self.data_hora_ini.minute,self.data_hora_fin.minute) - min(self.data_hora_ini.minute,self.data_hora_fin.minute))

    def __str__(self):
        return f"Cliente: \n{self.cliente}\nInterlocutor: {self.interlocutor}\nData e hora de comenzo: {self.data_hora_ini}\nData e hora de fin: {self.data_hora_fin}\nMinutos de chamada: {self.minutosChamada}\nSaínte: {self.sainte}"

class ChamadasRexistradas:
    def __init__(self, lista_chamadas=[]):
        self.lista_chamadas = lista_chamadas

    def engadirChamada(self, ag_chamada):
        if type(ag_chamada) == Chamada:
            self.lista_chamadas.append(ag_chamada)

    def listarChamadas(self,dni_query):
        lchamadas = ""
        for chamar in self.lista_chamadas:
            if chamar.cliente.dni == dni_query:
                lchamadas += str(chamar) + "\n\n"
        return lchamadas

    def calculoImpChamadas(self,dni_query):
        impchamadas = 0
        for chamar in self.lista_chamadas:
            if chamar.cliente.dni == dni_query:
                impchamadas += chamar.minutosChamada * 0.0002
        return f"{impchamadas}€"