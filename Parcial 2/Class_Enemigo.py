from MODO import *
from config import *
from Class_Personaje import *
from Class_Shagy import *
from Class_disparo import *

class Enemigo(Personaje):
    def __init__(self, acciones, escala, pos_x, pos_y, velocidad, posicion_x, posicion_y, plataformas_right_left, vida): 
        super().__init__(acciones, escala, pos_x, pos_y, velocidad)

        self.rectangulo = acciones["Quieto_derecha"][0].get_rect()
        self.rectangulo.width = 40
        self.rectangulo.height = 100
        self.rectangulo.x = posicion_x
        self.rectangulo.y = posicion_y

        self.rectangulo_base = acciones["Quieto_derecha"][0].get_rect()
        self.rectangulo_base.width = 40
        self.rectangulo_base.height = 10
        self.rectangulo_base.x = posicion_x
        self.rectangulo_base.y = posicion_y + 90

        self.pos_y = pos_y
        self.que_hace = "Enemigo_dispara"
        self.desplazamiento_y = 0
        self.limite_salto = 25

        self.lista_proyectiles = []
        self.flag_disparo = False
        self.plataformas_right_left = plataformas_right_left

        self.vida = vida
        self.enemigo_murio = False

        self.sound_flag = True
        self.sound_golpe_enemigo = pygame.mixer.Sound("Parcial 2/Recursos/Sonidos/Golpe shagy.mp3")
        self.sound_blood = pygame.mixer.Sound("Parcial 2/Recursos/Sonidos/blood.mp3")

    def colision_gravedad(self, plataforma):
        for piso in plataforma:
            if self.rectangulo_base.colliderect(piso):
                self.rectangulo_personaje.y = self.pos_y
                self.rectangulo_base.bottom = piso.top
                self.rectangulo.bottom = piso.top
                break
           
    def aplicar_gravedad_enemigo(self, plataforma):
        self.aplicar_gravedad()
        if self.desplazamiento_y <= self.limite_salto:
            self.desplazamiento_y += self.gravedad
        self.colision_gravedad(plataforma)
            
    def actualizar_pantalla(self, pantalla, plataforma, shagy):
        match self.que_hace:
            case "Enemigo_dispara":
                self.animar_personaje(pantalla)
                self.animacion_actual = self.acciones[self.que_hace]
            case "Enemigo_muere":
                if not self.enemigo_murio:
                    self.animar_personaje(pantalla)
                    
                    if self.sound_flag:
                        self.sound_blood.play()
                    self.sound_flag = False
                    if self.contador_pasos == 12:
                        self.enemigo_murio = True

                self.animacion_actual = self.acciones[self.que_hace]
        self.aplicar_gravedad_enemigo(plataforma)
        self.enemigo_muere()

        if self.contador_pasos == 18:
            self.flag_disparo = True
        if self.flag_disparo:
            self.actualizar_proyectiles(pantalla, shagy)

    def lanzar_proyectil(self, escala):
        x = None
        y = self.rectangulo.y
        if self.que_hace == "Quieto_derecha":
            x = self.rectangulo.right
        elif self.que_hace == "Enemigo_dispara":
            x = self.rectangulo.left - 100

        if x is not None:
            self.lista_proyectiles.append(Disparo(x, y, self.que_hace, escala))

    def actualizar_proyectiles(self, pantalla, shagy):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            pantalla.blit(p.item, p.rect_item)
            if obtener_modo():
                pygame.draw.rect(pantalla, (0,0,255), p.rect_item, 3)
            p.actualizar()

            if p.rect_item.colliderect(shagy.rectangulo) and not shagy.shagy_murio:
                pantalla.blit(p.item_golpe, p.rect_item)
                self.lista_proyectiles.pop(i)
                i -= 1
                shagy.vida -= 500
                if shagy.vida > 0:
                    self.sound_golpe_enemigo.play()
                

            if p.rect_item.centerx < 0 or p.rect_item.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1

            for piso in self.plataformas_right_left:
                if p.rect_item.colliderect(piso):
                    self.lista_proyectiles.pop(i)
                    i -= 1
            i += 1

    def enemigo_muere(self):
        if self.vida <= 0:
            self.que_hace = "Enemigo_muere"
            
