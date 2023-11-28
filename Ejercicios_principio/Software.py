import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo
desarrollo en python,
que promete revolucionar el mercado.
Las posibles aplicaciones son las siguientes:
    # Inteligencia artificial (IA),
    # Realidad virtual/aumentada (RV/RA),
    # Internet de las cosas (IOT) 
    # Procesamiento de lenguaje natural (NLP).


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:


A) Los datos a ingresar por cada empleado encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT, NLP)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
    1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y
    50 años inclusive.
    2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea
    Femenino o su edad se encuentre entre los 33 y 40.
    3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
    de ese género.
'''


lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta"]


lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49]
       
lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Femenino", "Masculino"]

lista_tecnologias = ["IA", "IA", "RV/RA", "NLP", "RV/RA", "NLP", "IOT", "IA", "NLP", "NLP"]

contador_while = 0
# while contador == 10:
#     nombre = prompt("Datos","Ingrese su nombre")
#     while not nombre.isalpha():
#         nombre = prompt("Datos","Ingrese un nombre valido")

#     edad = prompt("Datos","Ingrese su edad")
#     while not edad.isdigit() or int(edad) < 18:
#         edad = prompt("Datos","Ingrese una edad valida (+18)")

#     genero = prompt("Datos","Ingrese su genero")
#     while genero != "Maculino" and genero != "Femenino" and genero != "Otro":
#         genero = prompt ("Datos","Ingrese un genero valido")

#     tecnologia = prompt("Datos","Ingrese una tecnologia (IA, RV/RA, IOT, NLP)")
#     while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT" and tecnologia != "NLP":
#         tecnologia = prompt("Datos","Ingrese una tecnologia valida (IA, RV, RA, IOT, NLP)")

#     lista_nombres.append(nombre)
#     lista_edades.append(edad)
#     lista_generos.append(genero)
#     lista_tecnologias.append(tecnologia)
#     contador += 1



contador_masculino = 0
lista_punto_uno = []

for i in range(len(lista_nombres)):
    nombres = lista_nombres[i]
    edades = lista_edades[i]
    generos = lista_generos[i]
    votos = lista_tecnologias[i]


    match generos:
        case "Masculino":
            if votos == "IA" or votos == "IOT":
                if int(edades) <=50 and int(edades) >= 25:
                    contador_masculino += 1
                    lista_punto_uno.append(nombres)

for lista in lista_punto_uno:
    print(lista, end=' ')
print(f"La cantidad de epmleados masculinos de entre 25 y 50 años que votaron por IOT o IA es de {contador_masculino}")


