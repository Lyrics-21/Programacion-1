from MODO import *
from Class_Personaje import *
from Class_disparo import *
class Shagy(Personaje):
    def __init__(self, acciones, escala, pos_x, pos_y, velocidad, plataformas_right_left, vida): 
        super().__init__(acciones, escala, pos_x, pos_y, velocidad)

        self.rectangulo = acciones["Quieto_derecha"][0].get_rect()
        self.rectangulo.width = 45
        self.rectangulo.height = 110
        self.rectangulo.x = 110
        self.rectangulo.y = pos_y

        self.rectangulo_base = acciones["Quieto_derecha"][0].get_rect()
        self.rectangulo_base.width = 45
        self.rectangulo_base.height = 10
        self.rectangulo_base.x = 110
        self.rectangulo_base.y = pos_y + 110
        
        self.esta_saltando = False
        self.potencia_salto = -30
        self.desplazamiento_y = 0
        self.limite_salto = 25 
        self.esta_en_aire = False
        self.que_hace = "Quieto_derecha"

        self.lista_proyectiles = []
        self.plataformas_right_left = plataformas_right_left

        self.vida = vida
        self.shagy_murio = False
        self.flag_explosion = False
        self.sound_flag = True

        self.full_item = False

        self.sound_golpe_shagy = pygame.mixer.Sound("Parcial 2/Recursos/Sonidos/Golpe.mp3")
        self.sound_item = pygame.mixer.Sound("Parcial 2/Recursos/Sonidos/itemsound.mp3")
        self.sound_explosion = pygame.mixer.Sound("Parcial 2/Recursos/Sonidos/explosion.mp3")
        self.sound_muerte_shagy = pygame.mixer.Sound("Parcial 2/Recursos/Sonidos/muerte shagy.mp3")
        
    def mover_personaje(self, que_hace, plataformas_right_left):
        if que_hace == "Derecha":
            self.mover_personaje_derecha(plataformas_right_left)
        elif que_hace == "Izquierda":
            self.mover_personaje_izquierda(plataformas_right_left)
                
    def colision_gravedad(self, plataforma):
        for piso in plataforma:
            if self.rectangulo_base.colliderect(piso):
                self.esta_saltando = False
                self.esta_en_aire = False
                self.rectangulo_personaje.bottom = piso.top
                self.rectangulo_base.bottom = piso.top
                self.rectangulo.bottom = piso.top
                break
            else:
                self.esta_saltando = True
                self.esta_en_aire = True
  
    def aplicar_gravedad_shagy(self, pantalla, plataforma):
        if self.esta_saltando:
            self.animar_personaje(pantalla)
        self.aplicar_gravedad()
        if self.desplazamiento_y <= self.limite_salto:
            self.desplazamiento_y += self.gravedad
        self.colision_gravedad(plataforma)
            
    def actualizar_pantalla(self, pantalla, plataforma, plataformas_right_left, enemigos):
        match self.que_hace:
            case "Quieto_derecha":
                if not self.esta_en_aire:
                    self.animar_personaje(pantalla)
                self.animacion_actual = self.acciones[self.que_hace]
            case "Quieto_izquierda":
                if not self.esta_en_aire:
                    self.animar_personaje(pantalla)
                self.animacion_actual = self.acciones[self.que_hace]      
            case "Derecha":
                if not self.esta_en_aire:
                    self.animar_personaje(pantalla)
                self.mover_personaje(self.que_hace, plataformas_right_left)
                self.animacion_actual = self.acciones[self.que_hace]
            case "Izquierda":
                if not self.esta_en_aire:
                    self.animar_personaje(pantalla)
                self.mover_personaje(self.que_hace, plataformas_right_left)
                self.animacion_actual = self.acciones[self.que_hace]
            case "Salta_derecha":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.esta_en_aire = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.acciones[self.que_hace]
            case "Salta_izquierda":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.esta_en_aire = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.acciones[self.que_hace]
            case "Shagy_muere":
                if not self.shagy_murio:
                    self.animar_personaje(pantalla)
                    if self.sound_flag:
                        self.sound_explosion.play()
                        self.sound_muerte_shagy.play()
                    self.sound_flag = False
                    if self.contador_pasos == 24:
                        self.shagy_murio = True
                        self.sound_explosion.stop()
                    self.animacion_actual = self.acciones[self.que_hace]

        self.actualizar_proyectiles(pantalla, enemigos)
        self.shagy_muere()
        self.aplicar_gravedad_shagy(pantalla, plataforma)

    def colision_item(self, lista_items, lista_rect_item):
        for item, rect_item in zip(lista_items, lista_rect_item):
            if self.rectangulo.colliderect(rect_item):
                lista_items.remove(item)
                lista_rect_item.remove(rect_item)
                self.sound_item.play()
        if len(lista_items) == 0:
            self.full_item = True
    
    def lanzar_proyectil(self, escala):
        x = None
        margen = 40
        y = self.rectangulo.centery + 10
        if self.que_hace == "Derecha" or self.que_hace == "Quieto_derecha" or self.que_hace == "Salta_derecha":
            x = self.rectangulo.right - margen
        elif self.que_hace == "Izquierda" or self.que_hace == "Quieto_izquierda" or self.que_hace == "Salta_izquierda":
            x = self.rectangulo.left - 100 + margen
        
        if x is not None:
            self.lista_proyectiles.append(Disparo(x, y, self.que_hace, escala))

    def actualizar_proyectiles(self, pantalla, enemigos):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            pantalla.blit(p.item_shagy, p.rect_item)
            if obtener_modo():
                pygame.draw.rect(pantalla, (0,0,255), p.rect_item, 3)
            p.actualizar()
            for enemigo in enemigos:
                if p.rect_item.colliderect(enemigo.rectangulo) and not enemigo.enemigo_murio:
                    self.lista_proyectiles.pop(i)
                    i -= 1
                    enemigo.vida -= 250
                    self.sound_golpe_shagy.play()


            if p.rect_item.centerx < 0 or p.rect_item.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1

            for piso in self.plataformas_right_left:
                if p.rect_item.colliderect(piso):
                    self.lista_proyectiles.pop(i)
                    i -= 1
            i += 1

    def shagy_muere(self):
        if self.vida <= 0:
            self.que_hace = "Shagy_muere"
            self.flag_explosion = True

    def obtener_estado_salto(self):
        return self.esta_saltando