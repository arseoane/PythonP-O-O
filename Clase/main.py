from cono import Cono
from circulo import Circulo
from cilindro import Cilindro
from esfera import Esfera

print("Círculo: ")
print("Diámetro = ", Circulo.obterDiametro(10))
print("Perímetro = ", Circulo.perimetro(10))
print("Área = ", Circulo.calcularArea(10))

print("\nCilindro:")
print(Cilindro.propiedades_cilindro(10, 10))
print("Esfera:")
print(Esfera.propiedades_esfera(10))
print("\nCono:")
print(Cono.propiedades_cono(10,20))