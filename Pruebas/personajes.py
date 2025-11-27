class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        print(f"*** Nuevo personaje creado: {self.nombre} ***")

    def saludar(self):
        return f"Hola, soy {self.nombre} y mi vida actual es {self.vida}."

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        print(f"¡{self.nombre} ha recibido {cantidad} de daño! Vida restante: {self.vida}")