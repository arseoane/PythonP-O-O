from horastest import Horas

horas1 = Horas(23, 84, 20)
print(horas1.mostrarFormato12Horas())

horas1._Horas__asignacionHoraColeccion(3203)
horas1._Horas__asignacionMinutoColeccion(23)
print(horas1.mostrarFormato12Horas())

print(horas1.mostrarHoras())
print(horas1.mostrarMinutos())
print(horas1.mostrarSegundos())

horas2 = Horas(23, 48, 20)

horas2._Horas__asignacionHoraColeccion(23)

horas1._Horas__asignacionSegundoColeccion(100)

print(horas1.mostrarSegundos())

print(horas2.mostrarSegundos())

print(isinstance(horas1, Horas))

print(horas2.setHoras(932039))

horas2._Horas__asignacionHoraColeccion(23)