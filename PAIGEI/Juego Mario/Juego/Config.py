import pygame as py

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



personaje_quieto = [py.image.load(r"PAIGEI/Juego Mario/Recursos/0.png")]
personaje_camina_derecha = [py.image.load(r"PAIGEI/Juego Mario/Recursos/1.png"),
                            py.image.load(r"PAIGEI/Juego Mario/Recursos/2.png")]
personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta = [py.image.load(r"PAIGEI/Juego Mario/Recursos/3.png")]

enemigo_camina = [py.image.load("PAIGEI/Juego Mario/Recursos/a.jpeg"), py.image.load("PAIGEI/Juego Mario/Recursos/b.jpeg")]

enemigo_aplasta = [py.image.load("PAIGEI/Juego Mario/Recursos/c.jpeg")]

flor_fuego = [py.image.load("PAIGEI/Juego Mario/Recursos/p.jpeg")]

super_mario = [py.image.load("PAIGEI/Juego Mario/Recursos/super1.jpeg"), py.image.load("PAIGEI/Juego Mario/Recursos/super2.jpeg"), py.image.load("PAIGEI/Juego Mario/Recursos/super3.jpeg"), py.image.load("PAIGEI/Juego Mario/Recursos/super4.jpeg")]
