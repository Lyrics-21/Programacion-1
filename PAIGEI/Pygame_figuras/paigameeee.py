import pygame

BLANCO = (255,255,255)
NEGRO = (0,0,0,)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)


lista_nombres = ["Primer Puesto", "Segundo Puesto",]
a = "Tercer Puesto"

pygame.init()

VENTANA = pygame.display.set_mode((800,800)) #Pixeles
pygame.display.set_caption("TOP 3 Mejores Peliculas") #Titulo de ventana
icono = pygame.image.load("PAIGEI/Pygame_figuras/2.jpg") 
pygame.display.set_icon(icono)
VENTANA.fill(NEGRO) #Color del fondo
fuente = pygame.font.SysFont("Arial",40)


imagen1 = pygame.image.load("PAIGEI/Pygame_figuras/4.jpg")
imagen2 = pygame.image.load("PAIGEI/Pygame_figuras/3.jpg")
imagen3 = pygame.image.load("PAIGEI/Pygame_figuras/1.jpg")

# imagen1 = pygame.transform.flip(imagen1,True,False) #rotar imagen
# imagen1 = pygame.transform.rotate(imagen1,20) #rota la imagen en grados

imagen1 = pygame.transform.scale(imagen1,(250,250))
imagen2 =  pygame.transform.scale(imagen2,(250,250))
imagen3 = pygame.transform.scale(imagen3,(250,250))

VENTANA.blit(imagen3, (450,450))
VENTANA.blit(imagen2, (300,300))
VENTANA.blit(imagen1, (150,150))


flag = True
while flag:
    y = 100
    x = 150
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    for listita in lista_nombres:
        texto = fuente.render(listita,True,BLANCO,NEGRO)
        texto2 = fuente.render(a,True,BLANCO,NEGRO)
        VENTANA.blit(texto,(x,y))
        VENTANA.blit(texto2,(450,700))
        y += 300

    pygame.display.update()

pygame.quit()
