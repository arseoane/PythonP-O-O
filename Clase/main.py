from horas import Horas

hora1 = Horas(24, 1, 3)

print(hora1.getSegundos())
print(hora1.getMinutos())
print(hora1.getHoras())

hora1.setMinutos(3)
print(hora1.getMinutos())

print(hora1.converterMinutos())
print(hora1.converterSegundos())