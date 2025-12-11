from tests_ia import *

libro = Libro("One Piece", "Eichiiro Oda", 2006, 250, 5)

print(libro.amosarLibro())
coche = Coche()

print(coche.getVelocidade())
coche.acelerar(10)
print(coche.getVelocidade())

conta1 = Conta("Conta 1", 1, "Euro", 100)
print(conta1.info())
conta1.ingreso(1)
print(conta1.info())