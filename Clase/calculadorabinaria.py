class CalculadoraBinaria:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def operacion(self, operando):
        if operando == '+':
            return self.a + self.b
        elif operando == '-':
            return self.a - self.b
        elif operando == '*':
            return self.a * self.b
        elif operando == '/':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Erro: División por cero"
        else:
            return "Operación non válida"