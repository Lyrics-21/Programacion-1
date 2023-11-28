import pygame as py

def click_cursor(evento, x, y, width, height):
    flag = False
    pos_x = evento.pos[0]
    pos_y = evento.pos[1]
    if pos_x >= x and pos_x <= (x + width) and pos_y >= y and pos_y <= (y + height):
        flag = True
    return flag

def mostrar_menu(evento, lista_rectangulos, pantalla, menu, icono):
    flag = False
    for rectangulos in lista_rectangulos:
        rectangulo_icono = icono.get_rect()
        rectangulo_icono.y = rectangulos.y - 8
        rectangulo_icono.x = rectangulos.x - 80
        cursor = click_cursor(evento, *rectangulos)
        if cursor:
            pantalla.blit(menu, (0,0))
            pantalla.blit(icono, (rectangulo_icono.x, rectangulo_icono.y))
            flag = True
    return flag

def click_menu(evento, rectangulo_start, rectangulo_options, rectangulo_quit):
    retorno = ""
    if click_cursor(evento, *rectangulo_start):
        retorno = "start"
    elif click_cursor(evento, *rectangulo_options):
        retorno = "options"
    elif click_cursor(evento, *rectangulo_quit):
        retorno = "quit"
    return retorno

def crear_item(imagen : str, escala, x, y):
    item = py.image.load(imagen)
    item = py.transform.scale(item, (escala))
    rect_item = item.get_rect()
    rect_item.x = x
    rect_item.y = y
    return rect_item, item

def reescalar_resolucion_ojetos(lista_objeto, nueva):
    for objeto in lista_objeto:
        objeto.x = objeto.x * (nueva[0] / 1920)
        objeto.y = objeto.y * (nueva[1] / 1080)
        objeto.width = objeto.width * (nueva[0] / 1920)
        objeto.height = objeto.height * (nueva[1] / 1080)

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))
            
def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    return lista_imagenes

def mostrar_vida_personaje(pantalla, fuente, personaje):
    if personaje.vida <= 0:
        personaje.vida = 0
    vidas = fuente.render(str(personaje.vida), True, (255,255,255), None)
    pantalla.blit(vidas, (75, 8))
