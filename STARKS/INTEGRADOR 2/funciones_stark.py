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
        print("Los datos se normalizaron correctamente")
    else:
        print("Error, Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
    return verificar

# 1.1
def obtener_valor(diccionario : dict, key : str):
    for clave in diccionario:
        if len(diccionario) > 0 and clave == key:
            return True
        else:
            return False       
def iterar_lista_diccionarios(lista : list):
    for elementos in lista:
        valor = obtener_valor(elementos, "nombre")
    print(valor)

#1.2
def iterar_dict_name(diccionario : dict, key : str):
        print(f"Nombre : {diccionario[key]}")

def obtener_nombre(lista : list):
    for elementos in lista:
        valor = obtener_valor(elementos, "nombre")
        if valor:
            iterar_dict_name(elementos, "nombre")
        else:
            print(valor)

#2
def obtener_nombre_y_dato(lista : list, key, clave):
 
    for elementos in lista:
        valor = obtener_valor(elementos, "nombre")
        if valor:
            nombre = elementos["nombre"]
            if nombre == key:
                print(f"Nombre : {nombre} / {clave} : {elementos[clave]}")
        else:
            print(valor)

#3
def obtener_maximo(lista : list, key : str):
    mayor = 0
    for elementos in lista:
        if key not in elementos:
            return False
        else:
            variable = elementos[key]
            if type(variable) == float or type(variable) == int:
                if variable > mayor:
                    mayor = variable
            else:
                return False
    return mayor

#4
def obtener_minimo(lista : list, key : str):
    flag = True
    menor = 0
    for elementos in lista:
        variable = elementos[key]
        if type(variable) == float or type(variable) == int:
            if (variable < menor) or flag:
                menor = variable
                flag = False
        else:
            return False
    return menor

#5
def obtener_dato_cantidad(lista : list, key : str, valor : float):
    lista_de_superheroes_condicion = []
    for diccionario in lista:
        if key in diccionario:
            variable = diccionario[key]
            if variable == valor :
                lista_de_superheroes_condicion.append(diccionario["nombre"])
        else:
            return False
    return lista_de_superheroes_condicion

#6
def stark_imprimir_heroes(lista : list):
    if type(lista) == list:
        for i in lista:
            if len(i) > 0:
                print(i)
            else:
                return False
    else:
        print("ERROR")
        return False

#7
def sumar_dato_heroe(lista : list, key : str):
    total = 0
    for diccionario in lista:
        if key in diccionario:
            suma = diccionario[key]
            total += suma
        else:
            return False
    return total

#8
def dividir(dividendo : float, divisor: float):
    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor
    return resultado

#9
def calcular_promedio(lista : list, key : str):
    contador = len(lista)
    total = sumar_dato_heroe(lista, key)
    promedio = dividir(total, contador)
    return promedio

#10
def mostrar_promedio_dato(lista : list, key : str):
    for i in lista:
        if (type(i[key]) == int or type(i[key]) == float) and len(i) > 0:
            dato = calcular_promedio(lista, key)
        else:
            return False
    print(dato)

#11
def validar_entero(numero : str):
    if numero.isdigit():
        return True
    else:
        return False
    
#12
def imprimir_menu():
    menu = (
    "elija una opcion:\n"
    "1. Normalizar datos\n"
    "2. Nombre de cada superhéroe de género NB\n"
    "3. Superhéroe más alto de género F\n"
    "4. Superhéroe más alto de género M\n"
    "5. Superhéroe más débil de género M\n"
    "6. Superhéroe más débil de género NB\n"
    "7. Fuerza promedio de los Superhéroes de género NB\n"
    "8. Cuántos Superhéroes tienen cada tipo de color de ojos\n"
    "9. Cuántos Superhéroes tienen cada tipo de color de pelo\n"
    "10. Listar todos los Superhéroes agrupados por color de ojos\n"
    "11. Listar todos los Superhéroes agrupados por tipo de inteligencia\n"
    "12. Salir\n"
    )
    return menu

#13
def stark_menu_principal():
    menu = imprimir_menu()
    respuesta = input(menu)
    if validar_entero(respuesta) and int(respuesta) <= 12:
        respuesta = int(respuesta)
        return respuesta
    else:
        return False    

#14
def obtener_nombre_y_maximo_especifico(lista : list, genero : str, key : str):
    altura_maxima = []
    for recorrer in lista:
        if recorrer["genero"] == genero:
            altura_maxima.append(recorrer)
    mayor = obtener_maximo(altura_maxima, key)
    lista_maximo = obtener_dato_cantidad(altura_maxima, key, mayor)
    for i in lista_maximo:
        print(f"{i} - {mayor}")

def obtener_nombre_y_minimo_especifico(lista : list, genero : str, key : str):
    altura_minima = []
    for recorrer in lista:
        if recorrer["genero"] == genero:
            altura_minima.append(recorrer)
    menor = obtener_minimo(altura_minima, key)
    lista_minimo = obtener_dato_cantidad(altura_minima, key, menor)
    for i in lista_minimo:
        print(f"{i} - {menor}")

def cantidad_tipos_especifico(lista : list, key: str):
  tipos = {}
  for heroes in lista:
      variable = heroes[key]
      if variable in tipos:
          tipos[variable] += 1
      else:
          tipos[variable] = 1
  for lista in tipos:
      print(f"{lista} - {tipos[lista]}")

def agrupar_tipos_lista(lista : list, key: str):
  tipos = {}
  for heroes in lista:
      variable = heroes[key]
      nombre = heroes["nombre"]
      if variable in tipos:
          tipos[variable] += f", {nombre}"
      else:
          tipos[variable] = nombre
  for lista in tipos:
      print(f"{lista} - {tipos[lista]}")

def stark_marvel_app(lista : list):
    normalizado = False
    flag = False
    while True:
        respuesta = stark_menu_principal()
        if respuesta == 1:
            normalizado = stark_normalizar_datos(lista)
        elif normalizado:
            flag = True
        elif respuesta != 1 and respuesta != 12:
            print("Normalize los datos antes de elegir una opcion\n")
        if normalizado or flag or respuesta == 12:
            match respuesta:
                case 2:
                    for i in lista_personajes:
                        if i["genero"] == "NB":
                            print(f"{i['nombre']} es de genero NB")
                case 3:
                    obtener_nombre_y_maximo_especifico(lista_personajes, "F", "altura")
                case 4:
                    obtener_nombre_y_maximo_especifico(lista_personajes, "M", "altura")
                case 5:
                    obtener_nombre_y_minimo_especifico(lista_personajes, "M", "fuerza")
                case 6:
                    obtener_nombre_y_minimo_especifico(lista_personajes, "NB", "fuerza")
                case 7:
                    lista_genero = []
                    for i in lista_personajes:
                        if i["genero"] == "NB":
                            lista_genero.append(i)
                    mostrar_promedio_dato(lista_genero, "fuerza")
                case 8:
                    cantidad_tipos_especifico(lista_personajes, "color_ojos")
                case 9:
                    cantidad_tipos_especifico(lista_personajes, "color_pelo")
                case 10:
                    agrupar_tipos_lista(lista_personajes, "color_ojos")
                case 11:
                    agrupar_tipos_lista(lista_personajes, "inteligencia")
                case 12:
                    break





