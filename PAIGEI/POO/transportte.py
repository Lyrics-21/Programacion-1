class Transporte:
    def __init__(self, cantidad, velocidad):
        self.cantidad_pasajeros = cantidad
        self.velocidad = velocidad
    def avanzar(self):
        print(f"Avanza a {self.velocidad} km/h")
    def frenar(self):
        print("Esta frenado")
    def mostrar(self):
        print(f"Pasajeros - {self.cantidad_pasajeros} | Velocidad - {self.velocidad}")