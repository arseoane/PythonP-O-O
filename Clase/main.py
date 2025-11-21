from Clase.esfera import Esfera
from circulo import Circulo
from cilindro import Cilindro
from cono import Cono
from data import Fecha

print(Circulo.obterDiametro(10))
print(Circulo.perimetro(10))
print(Circulo.calcularArea(10))
print(Cilindro.propiedades_cilindro(10, 10))
print(Esfera.volumen(10))
print(Esfera.superficie(10))
print(Esfera.diametro((10)))
print(Cono.volumen(10,10))

fecha1 = Fecha(20,12,2012)

print(fecha1.toStr())