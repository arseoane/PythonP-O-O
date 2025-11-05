from validar_dni import validar_dni
from validar_persoa import validar_persoa
from letra_dni import calcular_letra_dni
from verif_dni import DNI

print(validar_dni.validar("99887766L"))

print(validar_persoa.validar_idade(100))
print(validar_persoa.validar_dni("11223344C"))

print(validar_persoa("Pepe",30,"34343434P").aCadea())

print(calcular_letra_dni.letra_dni(53863169))
print(verif_dni.)