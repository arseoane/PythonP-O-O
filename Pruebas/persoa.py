class Persoa:
    def __init__(self,nombre,idade,dni):
        self.nombre = nombre
        self.idade = idade
        self.dni = dni

    def cumprirAno(idade):
        if idade >= 110:
            idade += 1
        else:
            idade = idade

    def validar(dni):
        if len(dni) == 9 and dni[:8].isnumeric() and dni[-1].isupper():
            return dni
        else:
            return "00000000X"



