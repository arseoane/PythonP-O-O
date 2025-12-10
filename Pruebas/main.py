from tests_ia import Coche, Moto, Camion

# Crear objetos
coche = Coche("Seat", "León", 2022)
moto = Moto("Yamaha", "MT-07", 2023, "700cc")
camion = Camion("Volvo", "FH", 2020, carga_maxima=25000)

# Probar cada uno
coche.encender()
coche.acelerar(80)
coche.info()
print()

moto.info()
moto.hacer_caballito()
print()

camion.info()
camion.cargar(15000)
camion.cargar(12000)   # Debe fallar o quedarse en el máximo
camion.info()

print(coche.leerVel)