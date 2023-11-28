from classpaigame import *
ANCHO = 1000
ALTO = 500
FPS = 30
VELOCIDAD = 10
BLANCO = (255,255,255)
NEGRO = (0,0,0,)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

pygame.init()

#IMAGEN VERTICAL
imagen_vertical = Imagen((ANCHO//2, ALTO//2),(100,100),(VERDE,AZUL))

#IMAGEN HORIZONTAL
imagen_horizontal= Imagen((ANCHO-100, ALTO//2),(100,100),(ROJO,BLANCO))

#PANTALLA
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

SIZE = (1000,500)

pygame.init()
PANTALLA = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Simpsoms")

icono = pygame.image.load("PAIGEI/POOO/Recursos/icono_homero.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("PAIGEI/POOO/Recursos/fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, SIZE)
PANTALLA.blit(fondo, (0,0))

pygame.mixer.music.load("PAIGEI/POOO/Recursos/intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT() 

    PANTALLA.blit(fondo, (0,0))
    PANTALLA.blit(imagen_vertical.superficie, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.superficie, imagen_horizontal.rectangulo)
    imagen_vertical.detectar_colision(imagen_horizontal)
    
    #MOVE
    imagen_vertical.mover("Vertical", VELOCIDAD, PANTALLA)
    imagen_horizontal.mover("Horizontal", VELOCIDAD, PANTALLA)
    
    pygame.draw.line(PANTALLA ,AZUL, (ANCHO//2,0),(ANCHO//2,ANCHO),1)
    pygame.draw.line(PANTALLA, AZUL, (0,ALTO//2),(ANCHO,ALTO//2),2)

    pygame.display.update()

