from horas import Horas

hora1 = Horas(24, 1, 3)

print(hora1.getSegundos())
print(hora1.getMinutos())
print(hora1.getHoras())

hora1.setMinutos(3)
print(hora1.getMinutos())

print(hora1.converterMinutos(100))
print(hora1.converterSegundos(100))

hora1.incrementarSegundos(100)
print(hora1.converterSegundos(100))

print(hora1.mostrarFormato12Horas())