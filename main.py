'''Crear clase persoa onde teño propiedades nome, idade, dni, direccion e nacemento.

Añadir tres funciones:

aCadea()
comprobarIdade(edade)
comprobarDNI(dni)
'''

from persoa import Persoa

persoa1 = Persoa("Enrique",33,"47474747F","Av. Adriana Salte, 67", "Bolivia")

print(persoa1.aCadea())
print(persoa1.comprobarDNI(persoa1.dni))
print(persoa1.comprobarIdade(persoa1.idade))
