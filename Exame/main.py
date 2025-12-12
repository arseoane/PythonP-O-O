from clases import *

persoa1 = Persoa("Santi","12345678Z",36002)
persoa2 = Persoa("Enrique","12345678Z",36984)

print(persoa1.comparar(persoa2))

cliente1 = ClienteTel("Santi","12345678Z",36984,"+34 612 345 678")
cliente2 = ClienteTel("Adriana","87654321P",36995,"+34 912 345 678")

print(cliente1)

chamada1 = Chamada(cliente1, cliente2.numtelefono,datetime.datetime.now(), datetime.datetime.now(), True)
chamada2 = Chamada(cliente2, cliente1.numtelefono,datetime.datetime.now(), datetime.datetime.now(), False)
chamada3 = Chamada(cliente1, cliente2.numtelefono,datetime.datetime.now(), datetime.datetime.now(), False)
print(chamada1)

rexistro = ChamadasRexistradas([chamada1])
rexistro.engadirChamada(chamada2)
rexistro.engadirChamada(chamada3)
print("\n=== Búsqueda de chamadas ===")
print(rexistro.listarChamadas("12345678Z"))