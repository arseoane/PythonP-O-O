class Fecha:
    def __init__(self, dia, mes, anho):
        self.setM(mes)
        self.setA(anho)
        self.setD(dia) #importante que vaya al final ya que es necesario que .__m y .__a estén inicializados

    def __str__(self):
        return self.toStr()

    def toStr(self):
        return "Hoy es " + str(self.__d) + " de " + str(self.__m) + " del año " + str(self.__a)

    def setD(self,d):
        if self.__m in [1,3,5,7,8,10,12]:
            if d <= 31 and d > 0:
                self.__d=d
            else:
                self.__d=0

        elif self.__m == 2:
            if self.__a % 4 == 0 and (self.__a % 100 != 0 or self.__a % 400 == 0): #es bisiesto
                if d <= 29 and d > 0:
                    self.__d = d
                else: #no lo es
                    self.__d = 0
            else:
                if d <= 28 and d > 0:
                    self.__d = d
                else:  # no lo es
                    self.__d = 0

        else:
            if d <= 30 and d > 0:
                self.__d = d
            else:
                self.__d = 0


    def setM(self,m):
        if m <= 12 and m > 0:
            self.__m=m
        else:
            self.__m=0

    def setA(self,a):
        if a >= 0:
            self.__a = a
        else:
            self.__a = None

    def getD(self):
        return self.__d
    def getM(self):
        return self.__m
    def getA(self):
        return self.__a

    dia = property(getD,setD)
    mes = property(getM,setM)
    anho = property(getA,setA)