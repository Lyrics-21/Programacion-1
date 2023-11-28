import pygame as py
from pygame.locals import *
from Config import *
from os import system
system("cls")
from Class_personaje import Personaje
from MODO import *
from Class_enemigo import Enemigo

def crear_plataforma(visible, premio, tamaño,  x,  y, path=""):
    plataforma = {}
    if visible:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = py.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y
    plataforma["premio"] = premio
    return plataforma

#ANCHO W - ALTO H
W,H = 1200, 680
FPS = 18 #Para desacelerar la pantalla

py.init()
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode((W,H)) # En pixeles
py.display.set_caption("Juego Mario")

#FONDO
fondo = py.image.load(r"PAIGEI/Juego Mario/Recursos/fondo.jpg").convert()
fondo = py.transform.scale(fondo, (W,H))

contador_pasos = 0

diccionario = {}
diccionario["Quieto"] = personaje_quieto
diccionario["Derecha"] = personaje_camina_derecha
diccionario["Izquierda"] = personaje_camina_izquierda
diccionario["Salta"] = personaje_salta
diccionario["Super"] = super_mario
mario = Personaje(diccionario,(70,60),600,500,20)
reescalar_imagenes(diccionario, 80,70)

#PISO
#piso = py.Rect(0,620,W,20)
piso = crear_plataforma(True, False, (W,20), 0, H-60, r"PAIGEI/Juego Mario/Recursos/3.png")
plataforma_caño = crear_plataforma(True, False, (100,100), 700, 530, r"PAIGEI/Juego Mario/Recursos/p.jpeg")

plataforma_invisible = crear_plataforma(False, False, (220,20),893,459,r"PAIGEI/Juego Mario/Recursos/fondo.jpg")

premio = crear_plataforma(False, True, (70, 50), 655, 405, "")

flor = {}
flor["superficie"] = flor_fuego[0]
flor["superficie"] = py.transform.scale((flor["superficie"]), (60, 70))
flor["rectangulo"] = flor["superficie"].get_rect()
flor["rectangulo"].midbottom = premio["rectangulo"].midtop
flor["descubierta"] = False
flor["tocada"] = False

plataformas= [piso, plataforma_caño, plataforma_invisible, premio]

#ENEMIGOS

diccionario_animaciones = {"izquierda": enemigo_camina, "aplasta": enemigo_aplasta}

un_enemigo = Enemigo(diccionario_animaciones)

lista_enemigos = [un_enemigo]

que_hace = "Quieto"

flag = True

while flag:
    RELOJ.tick(FPS)
    for event in py.event.get():
        if event.type == QUIT:
            flag = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                cambiar_modo()

    teclas = py.key.get_pressed()

    if teclas[py.K_RIGHT]:
        mario.que_hace = "Derecha"
    elif teclas[py.K_LEFT]:
        mario.que_hace = "Izquierda"
    elif(teclas[py.K_SPACE]):
        mario.que_hace = "Salta"
    else:
       mario.que_hace = "Quieto"

    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"])
    if flor["descubierta"] and not flor["tocada"]:
        PANTALLA.blit(flor["superficie"], flor["rectangulo"])

    mario.romper_bloque(plataformas, flor)
    mario.verificar_colision_flor(flor)
    mario.verificar_colision_enemigo(lista_enemigos, PANTALLA)
    mario.actualizar(PANTALLA, plataformas)
    un_enemigo.actualizar(PANTALLA)

    for i in range(len(lista_enemigos)):
        if lista_enemigos[i].esta_muerto:
            del lista_enemigos[i]
            break
    
    if obtener_modo():
        
        #py.draw.rect(PANTALLA, "yellow", piso, 3)
        py.draw.rect(PANTALLA, "blue", mario.rectangulo_principal,3)

        for plataforma in plataformas:
            py.draw.rect(PANTALLA, "red", plataforma["rectangulo"], 3)

    py.display.update()

py.quit()
