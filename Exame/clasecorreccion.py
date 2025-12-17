import datetime

class Persoa:
    def __init__(self, nome, dni, codpostal):
        self.nome = nome
        self.dni = dni
        self.codpostal = codpostal

    def __eq__(self, outra):
        return self.dni == outra.dni

    def __str__(self):
        return f"Nome: {self.nome}\nDNI: {self.dni}\nCódigo Postal: {self.codpostal}"

class ClienteTel(Persoa):
    def __init__(self, nome, dni, codpostal, numtelefono):
        super().__init__(nome, dni, codpostal)
        if len(numtelefono) == 15 and numtelefono[0] == "+" and numtelefono[3] == " " and numtelefono[7] == " " and numtelefono[11] == " ":
            numtelsinesp = numtelefono.replace(" ", "").replace("+", "")
            if numtelsinesp.isdigit():
                self.numtelefono = numtelefono
            else:
                self.numtelefono = "+00 000 000 000"
        else:
            self.numtelefono = "+00 000 000 000"

    def __str__(self):
        return f"{super().__str__()}\nNúmero Teléfono: {self.numtelefono}"

class Chamada:
    def __init__(self, cliente, interlocutor, data_hora_ini, data_hora_fin, sainte):
        self.cliente = cliente
        self.interlocutor = interlocutor
        self.data_hora_ini = data_hora_ini if isinstance(data_hora_ini, datetime.datetime) else None
        self.data_hora_fin = data_hora_fin if isinstance(data_hora_fin, datetime.datetime) else None
        self.sainte = sainte

    def minutosChamada(self):
        if self.data_hora_ini and self.data_hora_fin:
            delta = self.data_hora_fin - self.data_hora_ini
            return max(int(delta.total_seconds() // 60), 0)
        return 0

    def __str__(self):
        return (
            f"Cliente: \n{self.cliente}\n"
            f"Interlocutor: {self.interlocutor}\n"
            f"Data e hora de comenzo: {self.data_hora_ini}\n"
            f"Data e hora de fin: {self.data_hora_fin}\n"
            f"Minutos de chamada: {self.minutosChamada()}\n"
            f"Saínte: {self.sainte}"
        )

class ChamadasRexistradas:
    def __init__(self, lista_chamadas=None):
        self.lista_chamadas = lista_chamadas if lista_chamadas is not None else []

    def engadirChamada(self, ag_chamada):
        if isinstance(ag_chamada, Chamada):
            self.lista_chamadas.append(ag_chamada)

    def listarChamadas(self, dni_query):
        lchamadas = ""
        for chamar in self.lista_chamadas:
            if chamar.cliente.dni == dni_query:
                lchamadas += "\n" + str(chamar) + "\n"
        return lchamadas

    def calculoImpChamadas(self, dni_query):
        impchamadas = 0
        for chamar in self.lista_chamadas:
            if chamar.cliente.dni == dni_query:
                impchamadas += chamar.minutosChamada() * 0.0002
        return f"{impchamadas}€"
