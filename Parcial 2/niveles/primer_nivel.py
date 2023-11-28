import pygame
from funciones import *
from config import *
from Class_Shagy import *
from Class_Enemigo import *

pygame.init()
monitor_info = pygame.display.Info()
W = monitor_info.current_w 
H = monitor_info.current_h
resolucion_nueva = (W, H)

fondo_in_game = pygame.image.load("Parcial 2/Recursos/Bakcgorund GOd.png")
fondo_in_game = pygame.transform.scale(fondo_in_game, (W, H))

#Plataformas in game
primera_plataforma = pygame.Rect(0, 770, 215, 310)
segunda_plataforma = pygame.Rect(350, 980, 105, 100)
tercera_plataforma = pygame.Rect(578, 770, 105, 310)
cuarta_plataforma = pygame.Rect(833, 660, 105, 420)
quinta_plataforma = pygame.Rect(1085, 876, 105, 205)
sexta_plataforma = pygame.Rect(1196, 552, 105, 105)
septima_plataforma = pygame.Rect(1347, 985, 105, 95)
octava_plataforma = pygame.Rect(1600, 552, 320, 105)
novena_plataforma = pygame.Rect(1815, 985, 105, 95)

primera_right = pygame.Rect(190, 770, 25, 310)

segunda_left= pygame.Rect(350, 980, 25, 100)
segunda_right = pygame.Rect(430, 980, 25, 100)

tercera_left = pygame.Rect(578, 770, 25, 310)
tercera_right = pygame.Rect(658, 770, 25, 310)

cuarta_left = pygame.Rect(833, 660, 25, 420)
cuarta_right = pygame.Rect(913, 660, 25, 420)

quinta_left = pygame.Rect(1085, 876, 25, 205)
quinta_right = pygame.Rect(1165, 876, 25, 205)

sexta_left = pygame.Rect(1196, 552, 25, 105)
sexta_right = pygame.Rect(1276, 552, 25, 105)

septima_left = pygame.Rect(1347, 985, 25, 95)
septima_right = pygame.Rect(1427, 985, 25, 95)

octava_left = pygame.Rect(1600, 552, 25, 105)

novena_left = pygame.Rect(1815, 985, 25, 95)
novena_right = pygame.Rect(1895, 985, 25, 95)

plataformas = [primera_plataforma,
               segunda_plataforma,
               tercera_plataforma,
               cuarta_plataforma,
               quinta_plataforma,
               sexta_plataforma,
               septima_plataforma,
               octava_plataforma,
               novena_plataforma]
reescalar_resolucion_ojetos(plataformas, resolucion_nueva)

plataformas_right_left =[primera_right,
                         segunda_left,
                         segunda_right,
                         tercera_left,
                         tercera_right,
                         cuarta_left,
                         cuarta_right,
                         quinta_left,
                         quinta_right,
                         sexta_left,
                         sexta_right,
                         septima_left,
                         septima_right,
                         octava_left,
                         novena_left,
                         novena_right]
reescalar_resolucion_ojetos(plataformas_right_left, resolucion_nueva)

# Items
rect_pancho, pancho = crear_item("Parcial 2/Recursos/Items/pancho.png", (55,40), 375, 910)
segundo_rect_pancho, segundo_pancho = crear_item("Parcial 2/Recursos/Items/pancho.png", (55,40), 605, 700)
tercer_rect_pancho, tearcer_pancho = crear_item("Parcial 2/Recursos/Items/pancho.png", (55,40), 1374, 915)
cuarto_rect_pancho, cuarto_pancho = crear_item("Parcial 2/Recursos/Items/pancho.png", (55,40), 1112, 806)
quinto_rect_pancho, quinto_pancho = crear_item("Parcial 2/Recursos/Items/pancho.png", (55,40), 1842, 482)
sexto_rect_pancho, sexto_pancho = crear_item("Parcial 2/Recursos/Items/pancho.png", (55,40), 1223, 482)

lista_rect_item = [rect_pancho,
                   segundo_rect_pancho,
                   tercer_rect_pancho,
                   cuarto_rect_pancho,
                   quinto_rect_pancho,
                   sexto_rect_pancho,]

lista_items = [pancho,
              segundo_pancho,
              tearcer_pancho,
              cuarto_pancho,
              quinto_pancho,
              sexto_pancho]

reescalar_resolucion_ojetos(lista_rect_item, resolucion_nueva)

#Enemigo
acciones_enemigo = {}
acciones_enemigo["Quieto_derecha"] = enemigo_quieto_izquierda
acciones_enemigo["Enemigo_dispara"] = enemigo_dispara
acciones_enemigo["Enemigo_muere"] = enemigo_muere
soldado = Enemigo(acciones_enemigo, (450,180), 1470, 405, 0, 1730, 450, plataformas_right_left, 500)
segundo_soldado = Enemigo(acciones_enemigo, (450,180), 1582, 840, 0, 1845, 885, plataformas_right_left, 500)
tercer_soldado = Enemigo(acciones_enemigo, (450,180), 602, 515, 0, 865, 560, plataformas_right_left, 500)

lista_enemigos = [soldado, segundo_soldado, tercer_soldado]

cadencia_disparo_enemigo = 0