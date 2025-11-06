'''Crear clase persoa onde teño propiedades nome, idade, dni, direccion e nacemento.

Añadir tres funciones:

aCadea()
comprobarIdade(edade)
comprobarDNI(dni)
'''
class Persoa:
    def __init__(self, nome, idade, dni, direccion, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.dni = dni
        self.direccion = direccion
        self.nacionalidade = nacionalidade

    def aCadea(self):
        cadea = f"Nome: {self.nome}\nIdade: {self.idade}\nDNI: {self.dni}\nDirección: {self.direccion}\nNacionalidade: {self.nacionalidade}"
        return cadea

    def comprobarIdade(self,idade):
        if idade > 110:
            return 0
        elif idade < 0:
            return 0
        else:
            return idade

    def comprobarDNI(self,dni):
        if len(dni) == 9 and str(dni[-1]).isupper() and dni[:8].isdigit():
            if str(self.numero_dni + self.letra_dni) == "TRWAGMYFPDXBNJZSQVHLCKE"[int(self.numero_dni) % 23]:
                return dni
            else:
                return "00000000X"
        else:
            return "00000000X"


    def __str__(self):
        return self.aCadea()

