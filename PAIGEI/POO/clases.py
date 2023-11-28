class Personaje:
    def __init__(self, id, nombre, puede_volar, usa_nano, poder): # Metodo constructor
        self.id = id
        self.nombre = nombre
        self.puede_volar = puede_volar
        self.usa_nano = usa_nano
        self.poder = poder
    def mostrar_descripcion(self):
        descripcion = f"{self.id} - {self.nombre} - {self.puede_volar} - {self.usa_nano}"
        return descripcion
    def fight(self, otro_personaje):
        print(f"{self.nombre} VS. {otro_personaje.nombre}")
        if (self.poder > otro_personaje.poder):
            print(f"Gano : {self.nombre}")
        elif (self.poder < otro_personaje.poder):
            print(f"Gano : {otro_personaje.nombre}")
        else:
            print("Hubo Empate")
