from funciones import *
import pygame
class Disparo:
    def __init__(self, x, y, direccion, escala):
        self.rect_item, self.item = crear_item("Parcial 2/Recursos/Items/Proyectil.png", escala, x, y)
        self.rect_item, self.item_shagy = crear_item("Parcial 2/Recursos/Items/pancho.png", escala, x, y)
        self.item_golpe = pygame.image.load("Parcial 2/Recursos/Items/golpe.png")
        self.item_golpe = pygame.transform.scale(self.item_golpe, (130, 120))
        self.direccion = direccion

    def actualizar(self):
        if self.direccion == "Derecha" or self.direccion == "Quieto_derecha" or self.direccion == "Salta_derecha":
            self.rect_item.x += 30
        elif self.direccion == "Izquierda" or self.direccion == "Quieto_izquierda" or self.direccion == "Salta_izquierda" or self.direccion == "Enemigo_dispara":
            self.rect_item.x -= 30