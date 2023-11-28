lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]


lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
                    32, 22, 29, 27, 19, 49, 27, 22, 49, 27]
       
lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
                       "Otro", "Femenino", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
                        "Femenino", "Masculino", "Otro"]
       
lista_tecnologias = ["IOT", "RV/RA", "NLP", "IA", "NLP", "IOT", "RV/RA", "IOT", "IA", "NLP",
                    "RV/RA", "RV/RA", "NLP", "RV/RA", "IA", "IOT", "NLP", "IOT", "IA", "IA"]  
for i in range(len(lista_tecnologias)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    print(f"{nombre:15} {edad}\t{genero:15}{tecnologia}")
#1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.=

contador1 = 0

for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and (edad >= 25 and edad <= 50):
        contador1+=1

print(f"La cantidad de hombres que votaron IOT o IA cuya edad esta entre 25 y 50 años es de: {contador1}")
#2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.

cantidad_de_empleados = 0
porcentaje_de_empleados = 0

for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    if tecnologia != "IA" and genero != "Femenino" and (edad > 33 and edad < 40):
        cantidad_de_empleados += 1

porcentaje_de_empleados = (100*cantidad_de_empleados) / len(lista_generos)

print(f"El porcentaje de empleados que cumple con los requisitos de la encuesa es de: {porcentaje_de_empleados}%")

#3) - Nombre y tecnología de los votantes masculinos con mayor edad de ese género.

bandera = True
edad_maxima_masculino = 0

for i in range(len(lista_tecnologias)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    if bandera or (edad > edad_maxima_masculino and genero == "Masculino"):
        bandera = False
        edad_maxima_masculino=edad
        
for i in range(len(lista_tecnologias)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    if edad == edad_maxima_masculino and genero == "Masculino":
        print(f"{nombre:15} \t{genero}")

        
for i in range(10):
    nombre = input("Ingrese el nombre del empleado: ")
    while nombre != None and not nombre.isalpha():
        nombre = input("Reingrese el nombre del empleado: ")
    edad = input("Ingrese la edad del empleado: ")
    while(edad != None and not edad.isdigit()) or int(edad) < 18:
        edad = input("Reingrese la edad del empleado (Mayor a 18): ")
    edad = int(edad)
    genero = input("Ingrese el genero del empleado: ")
    while(genero != None and genero.isalpha()) and genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Reingrese el genero del empleado: ")
    tecnologia = input("Ingrese la tecnologia del empleado: ")
    while (tecnologia != None and not tecnologia.isalpha()) and tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT" and tecnologia != "NLP":
        tecnologia = input("Reingrese la tecnologia del empleado: ")
    
    lista_nombres.append(nombre)
    lista_edades.append(edad)
    lista_generos.append(genero)
    lista_tecnologias.append(tecnologia)

# print(f"{nombre:15} {edad}\t {a}")  #esto genera 15 espacions u una tabulacion