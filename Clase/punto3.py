class Punto3:
    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        if type(x) == int or type(x) == float:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError(f"O valor de x = {x} non pertence ao primeiro cadrante.")
        else:
            raise TypeError("O tipo da coordenada x ten que ser int ou float")

    def setY(self, y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError(f"O valor de y = {y} non pertence ao primeiro cadrante.")
        else:
            raise TypeError("O tipo da coordenada y ten que ser int ou float")

    def __str__(self):
        return f"X: {self.__x}\nY: {self.__y}"

punto3 = Punto3(1, 2)
print(punto3)