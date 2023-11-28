import pygame
from funciones import *
from config import *
from Class_Shagy import *
from Class_Enemigo import *
from Class_disparo import *
from MODO import *

from niveles.primer_nivel import*

FPS = 30
   
pygame.init()
pygame.mixer.init()

RELOJ = pygame.time.Clock()

monitor_info = pygame.display.Info()
W = monitor_info.current_w 
H = monitor_info.current_h

resolucion_nueva = (W, H)

PANTALLA = pygame.display.set_mode((W,H))
pygame.display.set_caption("Blackout")

fuente = pygame.font.SysFont("impact",50)

#Menu
sound_menu = pygame.mixer.Sound("Parcial 2/Recursos/Menu/Sounds/Sound_menu.mp3")
sound_menu_click = pygame.mixer.Sound("Parcial 2/Recursos/Menu/Sounds/Sound_menu2.mp3")
sound_flag_menu = True

menu_activo = True
menu = pygame.image.load("Parcial 2/Recursos/Menu/menu_god.png")
menu = pygame.transform.scale(menu,(W,H))
icono = py.image.load("Parcial 2/Recursos/Menu/icon.png")
icono = py.transform.scale(icono, (80,80))

PANTALLA.blit(menu, (0,0))
# Opciones menu
rectangulo_start = py.Rect(595, 425, 712, 42)
rectangulo_options = py.Rect(710, 510, 480, 42)
rectangulo_quit = py.Rect(640, 600, 622, 42)

rectangulos_menu = [rectangulo_start,
                    rectangulo_options,
                    rectangulo_quit]
reescalar_resolucion_ojetos(rectangulos_menu, resolucion_nueva)

#Personaje
acciones = {}
acciones["Quieto_derecha"] = personaje_quieto_derecha
acciones["Quieto_izquierda"] = personaje_quieto_izquierda
acciones["Derecha"] = personaje_camina_derecha
acciones["Izquierda"] = personaje_camina_izquierda
acciones["Salta_derecha"] = personaje_salta_derecha
acciones["Salta_izquierda"] = personaje_salta_izquierda
acciones["Shagy_muere"] = explosion
ultima_posicion = "Derecha"

shagy = Shagy(acciones, (130,120), 70, 650, 15, plataformas_right_left, 1500)
reescalar_imagenes(acciones, 130, 120)
sound_pasos = pygame.mixer.Sound("Parcial 2/Recursos/Sonidos/run.mp3")

sound_flag = True
#Disparo
cadencia_disparo = 0
contador = 0
flag = True
while flag:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                PANTALLA.blit(menu, (0,0))
                menu_activo = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()

    if menu_activo:
        if event.type == pygame.MOUSEMOTION:
            menu_flag = mostrar_menu(event, rectangulos_menu, PANTALLA, menu, icono)
            if menu_flag:
                if sound_flag_menu:
                    sound_menu.play()
                sound_flag_menu = False
            else:
                sound_flag_menu = True
                PANTALLA.blit(menu, (0,0))

        if event.type == pygame.MOUSEBUTTONUP:
            click = click_menu(event, rectangulo_start, rectangulo_options, rectangulo_quit)
            match click:
                case "start":
                    sound_menu_click.play()
                    menu_activo = False
                case "options":
                    sound_menu_click.play()
                    menu_activo = False
                case "quit":
                    flag = False
        
    if not menu_activo:
        teclas = pygame.key.get_pressed()
        estado_salto = shagy.obtener_estado_salto()
        if not shagy.flag_explosion:
            if teclas[py.K_RIGHT]:
                shagy.que_hace = "Derecha"
                ultima_posicion = "Derecha"
                if sound_flag:
                    sound_pasos.play()
                sound_flag = False
            elif teclas[py.K_LEFT]:
                shagy.que_hace = "Izquierda"
                ultima_posicion = "Izquierda"
                if sound_flag:
                    sound_pasos.play()
                sound_flag = False
            else:
                if estado_salto:
                    sound_flag = True
                    sound_pasos.stop()
                    if ultima_posicion == "Derecha":
                        shagy.que_hace = "Salta_derecha"
                    else:
                        shagy.que_hace = "Salta_izquierda"
                elif not estado_salto:
                    sound_flag = True
                    sound_pasos.stop()
                    if ultima_posicion == "Derecha":
                        shagy.que_hace = "Quieto_derecha"
                    else:
                        shagy.que_hace = "Quieto_izquierda"

            if teclas[pygame.K_e]:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - cadencia_disparo >= 300:
                    shagy.lanzar_proyectil((26,26))
                    cadencia_disparo = tiempo_actual

            if teclas[py.K_SPACE] and not estado_salto:
                if ultima_posicion == "Derecha":
                    shagy.que_hace = "Salta_derecha"
                else:
                    shagy.que_hace = "Salta_izquierda"
        else:
            sound_flag = True
            sound_pasos.stop()

        ###################################################################################################
        if not shagy.full_item:
            PANTALLA.blit(fondo_in_game,(0,0))
            mostrar_vida_personaje(PANTALLA, fuente, shagy)
            largo = len(lista_corazones)
            if contador >= largo:
                contador = 0
            PANTALLA.blit(lista_corazones[contador], (10, 10))
            contador += 1

            shagy.actualizar_pantalla(PANTALLA, plataformas, plataformas_right_left, lista_enemigos)
            
            for item, rect_item in zip(lista_items, lista_rect_item):
                PANTALLA.blit(item, (rect_item.x, rect_item.y))
            shagy.colision_item(lista_items, lista_rect_item)
            
            soldado.actualizar_pantalla(PANTALLA, plataformas, shagy)
            segundo_soldado.actualizar_pantalla(PANTALLA, plataformas, shagy)
            tercer_soldado.actualizar_pantalla(PANTALLA, plataformas, shagy)

            tiempo_actual_enemigo = pygame.time.get_ticks()
            if tiempo_actual_enemigo - cadencia_disparo_enemigo >= 1100:
                soldado.lanzar_proyectil((28,28))
                segundo_soldado.lanzar_proyectil((28,28))
                tercer_soldado.lanzar_proyectil((28,28))
                cadencia_disparo_enemigo = tiempo_actual_enemigo
        ###################################################################################################

        elif shagy.full_item:
            PANTALLA.blit(menu,(0,0))
    if obtener_modo():
        #########################################################################
        if menu_activo:
            for draw_menu in rectangulos_menu:
                pygame.draw.rect(PANTALLA, (0,255,0), draw_menu, 3)
        if not shagy.full_item and not menu_activo:
            pygame.draw.rect(PANTALLA, (0,0,255), shagy.rectangulo, 3)
            pygame.draw.rect(PANTALLA, (255,255,255), shagy.rectangulo_base, 3)

            pygame.draw.rect(PANTALLA, (0,0,255), soldado.rectangulo, 3)
            pygame.draw.rect(PANTALLA, (0,0,255), segundo_soldado.rectangulo, 3)
            pygame.draw.rect(PANTALLA, (0,0,255), tercer_soldado.rectangulo, 3)
            pygame.draw.rect(PANTALLA, (255,255,255), soldado.rectangulo_base, 3)
            pygame.draw.rect(PANTALLA, (255,255,255), segundo_soldado.rectangulo_base, 3)
            pygame.draw.rect(PANTALLA, (255,255,255), tercer_soldado.rectangulo_base, 3)
            
            for draw_plataformas in plataformas:
                pygame.draw.rect(PANTALLA, (200,0,0), draw_plataformas, 3)
            for draw_right_left in plataformas_right_left:
                pygame.draw.rect(PANTALLA, (0,0,255), draw_right_left, 3)
            for item in lista_rect_item:
                pygame.draw.rect(PANTALLA, (0,0,255), item, 3)
     
        ##########################################################################

    pygame.display.update()
pygame.quit()
