import pygame
import math
#from funciones_paigame import perimetro_area_texto

BLANCO = (255,255,255)
NEGRO = (0,0,0,)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

pygame.init()

VENTANA = pygame.display.set_mode((800,800)) #Pixeles
icono = pygame.image.load("PAIGEI/2.jpg") 
pygame.display.set_icon(icono)
VENTANA.fill(NEGRO) #Color del fondo
imagen1 = pygame.image.load("PAIGEI/4.jpg")
imagen1 = pygame.transform.scale(imagen1,(800,800))
VENTANA.blit(imagen1, (0,0))


#Fiuguras
x = 400
y = 400
a = 600

radio = 150

puntos_triangulo = [(400, 200), (200, 500), (600, 500)]

figura = "Rectangulo"

fuente = pygame.font.SysFont("Arial",50)

# circulo
def perimetro_area_texto():
    flag = True
    while flag:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag = False
                
        match figura:
            case "Circulo":
                pygame.draw.circle(VENTANA, ROJO, (x, y), radio)
                area = math.pi * (radio**2)
                perimetro = (math.pi * 2) * radio
            case "Cuadrado":
                pygame.draw.rect(VENTANA, ROJO, (200, 150, x, y))
                area = x * y
                perimetro = (x + y) * 2
            case "Rectangulo":
                pygame.draw.rect(VENTANA, ROJO, (110, 150, a, x),)
                area = area = x * a
                perimetro = (x + a) * 2
            case "Triangulo":
                pygame.draw.polygon(VENTANA, ROJO, puntos_triangulo)
                area = a
                perimetro = a

        texto1 = fuente.render(f"Perimetro : {perimetro} px",True,ROJO, NEGRO)
        texto2 = fuente.render(f"Area: {area} px",True,ROJO, NEGRO)
        VENTANA.blit(texto1,(50,650))
        VENTANA.blit(texto2,(50,700))
        pygame.display.update()
    pygame.quit()
    return area, perimetro

perimetro_area_texto()

      

