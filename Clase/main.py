from Clase.cono import Cono
from circulo import Circulo
from cilindro import Cilindro
from esfera import Esfera

print(Circulo.obterDiametro(10))
print(Circulo.perimetro(10))
print(Circulo.calcularArea(10))

print("\nCilindro:")
print(Cilindro.propiedades_cilindro(10, 10))
print("\nEsfera:")
print(Esfera.propiedades_esfera(10))
print("\nCono:")
print(Cono.propiedades_cono(10,20))