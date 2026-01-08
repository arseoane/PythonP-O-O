class CalculadoraBinaria:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

    def operacion(self, operando):
        if operando == '+':
            return self.__a + self.__b
        elif operando == '-':
            return self.__a - self.__b
        elif operando == '*':
            return self.__a * self.__b
        elif operando == '/':
            if self.__b != 0:
                return self.__a / self.__b
            else:
                return "Erro: División por cero"
        else:
            return "Operación non válida"