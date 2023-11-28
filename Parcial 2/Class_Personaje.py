from funciones import reescalar_imagenes
class Personaje:
    def __init__(self, acciones, escala, pos_x, pos_y, velocidad):
        self.acciones = acciones # Diccionario de moviemientos del personaje
        reescalar_imagenes(acciones, *escala)
        # Rectangulo del personaje
        self.rectangulo_personaje = acciones["Quieto_derecha"][0].get_rect() #Usar rectangulos en diccionarios
        self.rectangulo_personaje.width = 85
        self.rectangulo_personaje.height = 109
        self.rectangulo_personaje.x = pos_x
        self.rectangulo_personaje.y = pos_y
        self.contador_pasos = 0
        self.animacion_actual = acciones["Quieto_derecha"]
        self.velocidad = velocidad
        self.gravedad = 2

    def animar_personaje(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_personaje)
        self.contador_pasos += 1
    
    def mover_personaje_derecha(self, plataformas_right_left):
        self.rectangulo_personaje.x += self.velocidad
        self.rectangulo.x += self.velocidad
        self.rectangulo_base.x += self.velocidad

        for piso in plataformas_right_left:
            if self.rectangulo.colliderect(piso):
                self.rectangulo.right = piso.left
                self.rectangulo_base.right = piso.left
                self.rectangulo_personaje.right = self.rectangulo.right

    def mover_personaje_izquierda(self, plataformas_right_left):
        x_izquierda = self.rectangulo.left
        if x_izquierda > 0:
            self.rectangulo_personaje.x -= self.velocidad
            self.rectangulo.x -= self.velocidad
            self.rectangulo_base.x -= self.velocidad

        for piso in plataformas_right_left:
            if self.rectangulo.colliderect(piso):
                self.rectangulo.left = piso.right
                self.rectangulo_base.left = piso.right
                self.rectangulo_personaje.right = self.rectangulo.right

    def aplicar_gravedad(self):
        self.rectangulo_personaje.y += self.desplazamiento_y
        self.rectangulo.y += self.desplazamiento_y
        self.rectangulo_base.y += self.desplazamiento_y



    
