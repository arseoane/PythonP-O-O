from clasecorreccion import *

p1 = Persona("Ana", "12345678A", "12/12345678/90", "+34 123 456 789")
p2 = Persona("Luis", "12345678A", "mal", "incorrecto")

print(p1.nuss)
print(p2.nuss)
print(p2.telefono)
print(p1 == p2)