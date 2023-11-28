from data_stark import lista_personajes

def stark_normalizar_datos(lista : list):
    for variables in lista:
        if "altura" not in variables or "peso" not in variables or "fuerza" not in variables:
            return False
        else:
            if type(variables["altura"]) == int or type(variables["altura"]) == float or variables["altura"] == "":
                verificar = False
            else:
                variables["altura"] = float(variables["altura"])
                verificar = True

            if type(variables["peso"]) == int or type(variables["peso"]) == float or variables["peso"] == "":
                verificar = False
            else:
                variables["peso"] = float(variables["peso"])
                verificar = True
            
            if type(variables["fuerza"]) == int or type(variables["fuerza"]) == float or variables["fuerza"] == "":
                verificar = False
            else:
                variables["fuerza"] = int(variables["fuerza"])
                verificar = True

    if verificar:
        print("los datos se normalizaron correctamente")
    else:
        print("Error, Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
    return verificar


flag_altura = True
altura_menor = 0
fuerza_mayor = 0

peso_total = 0
promedio_peso = 0 
contador_peso = 0

fuerza_total = 0
promedio_fuerza = 0
contador_fuerza = 0

normalizado = False
flag = False

while True:
    respuesta = input("\nSeleccione una opcion:\n\n\
A: Normalizar datos\n\n\
B: Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe\n\n\
C: Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza\n\n\
D: Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo\n\n\
E: Recorrer la lista y determinar el peso promedio de los superhéroes masculinos\n\n\
F: Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género)\n\
   los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino\n\n\
G: Salir\n")

    if respuesta == "1":
      normalizado = stark_normalizar_datos(lista_personajes)
    elif normalizado:
       flag = True

    if respuesta == "G" or normalizado or flag:
      match respuesta:
          case "B": # A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
              for lista in lista_personajes:
                nombres = lista["nombre"]
                identidades = lista["identidad"]
                empresas = lista["empresa"]
                alturas = lista["altura"]
                pesos = lista["peso"]
                generos = lista["genero"]
                ojos = lista["color_ojos"]
                pelo = lista["color_pelo"]
                fuerzas = lista["fuerza"]
                inteligencias = lista["inteligencia"]

                print(f"\n\
                Nombre = {nombres}\n\
                Identidad = {identidades}\n\
                Empresa = {empresas}\n\
                Altura = {alturas}\n\
                Peso = {pesos}\n\
                Genero = {generos}\n\
                Color de ojos = {ojos}\n\
                Color de pelo = {pelo}\n\
                Fuerza = {fuerzas}\n\
                Inteligencia = {inteligencias}\n")

          case "C": # B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza
            for lista in lista_personajes:
              fuerzas = lista["fuerza"]
              if fuerzas > fuerza_mayor:
                fuerza_mayor = fuerzas

            for lista in lista_personajes: #Para imprimir el nombre de la o las personas con mas fuerza
              nombres = lista["nombre"]
              identidades = lista["identidad"]
              pesos = lista["peso"]
              fuerzas = lista["fuerza"]
              if fuerzas == fuerza_mayor:
                print(f"{identidades}\nAlias - {nombres}\nPesa {pesos} kg\n" )

            print( f"Tiene/n {fuerza_mayor} puntos de fuerza\n\n")
            
          case "D":
            for lista in lista_personajes: # C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
              alturas = lista["altura"]

              if flag_altura or alturas < altura_menor:
                flag_altura = False
                altura_menor = alturas

            for lista in lista_personajes: #Para imprimir el nombre de la o las personas con mas fuerza
              nombres = lista["nombre"]
              identidades = lista["identidad"]
              alturas = lista["altura"]
              fuerzas = lista["fuerza"]
              
              if alturas == altura_menor:
                print(f"{identidades}\nAlias - {nombres} mide/n {altura_menor} cm" )

          case "E": # D. Recorrer la lista y determinar el peso promedio de los superhéroes
            for lista in lista_personajes:
              pesos = lista["peso"]
              generos = lista["genero"]

              if generos == "M":
                peso_total += pesos
                contador_peso += 1

            promedio_peso = peso_total / contador_peso
            print(f"El peso promedio de los superheroes Masculinos es de {promedio_peso} kg\n")

          case "F":
            for lista in lista_personajes: #Para sacar el pronedio de la o las Heroinas con mas fuerza
              fuerzas = lista["fuerza"]
              generos = lista["genero"]

              if generos == "F":
                fuerza_total += fuerzas
                contador_fuerza += 1

            promedio_fuerza = fuerza_total / contador_fuerza
            print("Los Superheroses que superan el promedio de la fuerza total femenina son:\n")
            for lista in lista_personajes: #Punto E
              nombres = lista["nombre"]
              pesos = lista["peso"]
              fuerzas = lista["fuerza"]

              if fuerzas > promedio_fuerza:
                print(f"{nombres} - {pesos} kg")

          case "G":
            break
    else:
      print("Normalize los datos antes de elegir una opcion")


    






