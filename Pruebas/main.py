from persoa import Persoa
from coche import Coche

p1 = Persoa("Antonio",109,"12345678Z")

Persoa.cumprirAno(p1.idade)
print(p1.idade)
Persoa.cumprirAno(p1.idade)
print(p1.idade)
print("Coche:", Coche.mostrar_info("ferrari","450","2023"))