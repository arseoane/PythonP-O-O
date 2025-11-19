from persoa import Persoa
from coche import Coche
from contabanco import ContaBancaria
from rectangulo import Rectangulo

p1 = Persoa("Antonio",109,"12345678Z")

Persoa.cumprirAno(p1.idade)
print(p1.idade)
Persoa.cumprirAno(p1.idade)
print(p1.idade)
print("Coche:", Coche.mostrar_info("Ferrari","450","2023"))
print("\n")
cliente = ContaBancaria("Enrique")
print(cliente.mostrar_saldo())
cliente.depositar(3)
print(cliente.mostrar_saldo())
cliente.depositar(3)
print(cliente.mostrar_saldo())
cliente.retirar(4)
print(cliente.mostrar_saldo())

print("\n")
r1 = Rectangulo(10, 20)
print(r1.area())