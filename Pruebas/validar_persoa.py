class validar_persoa:
    def __init__(self, nome, idade, dni):
        self.nome = nome
        if idade >= 0 and idade <= 110:
            self.idade = idade
        else:
            self.idade = 0

        if len(dni) == 9 and dni[:8].isnumeric() and dni[-1].isalpha() and dni[-1].isupper():
            self.dni = dni
        else:
            self.dni = "XXXXXXXXX"

    def validar_idade(idade):
        if idade >= 0 and idade <= 110:
            return idade
        else:
            return 0

    def validar_dni(dni):
        if str(dni)[:8].isnumeric() and str(dni)[-1].isalpha() and str(dni)[-1].isupper and len(str(dni)) == 9:
            return dni
        else:
            return "XXXXXXXXX"

    def aCadea(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nDNI: {self.dni}"
