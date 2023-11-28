import re
from data_stark import lista_personajes

#1.1
def extraer_iniciales(nombre: str): # Funcion para etraer las iniciales de un nombre
    if nombre == " " or nombre == "": # si nombre esta vacio o tiene un espacio en blanco entonces retorna "N/A"
        return "N/A"
    else:
        lista_palabras = re.findall("[a-zA-Z]{3,}", nombre) # De lo contrario divide la cadena de strings de a minimo 3 letras para evitar los articulos y demas
        iniciales = []
        for inicial in lista_palabras:
            if inicial.lower() != "the": # recorro la lista y si no hay un "the" entro al if
                iniciales.append(inicial[0].upper()) # appendeo la primera posicion de la lista y con el upper me aseguro que este todo en mayus
        lista = ".".join(iniciales) + "." # le agrego un "." al inicio con join y al final de la letra
        return lista
    
#1.2
def obtener_dato_formato(dato : str): # Esta funcion convierte cualquier cadena de texto en formate Snake_case
    if type(dato) is str: #valido si dato es de tipo String
        snake_case = re.sub("\\s", "_", dato) #con el sub reemplazo cualquier espacio en blanco por un "_"
        snake_case = snake_case.lower() #convierto todo a miniscula
        return snake_case
    
#1.3
def stark_imprimir_nombre_con_iniciales(nombre_heroe : dict): # devuelve el nombre en formato Snake_Case y ademas las iniciales
    if (type(nombre_heroe) is dict) and "nombre" in nombre_heroe: # Valida si la variable nombre_heroes es de tipo diccionario y si la key "nombre" existe dentro de ese diccionario
        nombre = nombre_heroe["nombre"] # asigna la key auna variable
        iniciales = extraer_iniciales(nombre) # reutilizo las funciones anteriores
        nombre = obtener_dato_formato(nombre)
        cadena = f"* {nombre} ({iniciales})"
    else:
        return False
    return cadena

#1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes : list): # Esta funcion hace exactamente lo mismo que la anterior pero ahora con una lista que contiene diccionarios
    lista_datos = []
    if type(lista_heroes) is list and len(lista_heroes) > 0: # valida si es de tipo lista y que la lista no esta vacia
        for diccionario in lista_heroes: # recorre la lista
            cadena = stark_imprimir_nombre_con_iniciales(diccionario) # Reutilizo la funcion anterior}
            lista_datos.append(cadena)
    else:
        return False
    return lista_datos

#2.1
def generar_codigo_heroe(diccionario : dict, id : int): #genera un codigo dependiendo del genero
    genero = diccionario["genero"] #asigna la key genero a una variable
    digito = 0
    match (genero): # dependiendo del genero si asigna un valor distinto a digito
        case "M":
            digito = "M-1"
        case "F":
            digito = "F-20"
        case "NB":
            digito = "NB-0"
    cantidad_digitos = len(digito) # asigno el rango de suma_cadena a una variable
    cantidad_ceros = 10 - cantidad_digitos # el rango maximo es 10, entonces resto la variable anterior a 10 para sabe la cantidad de 0
    ceros = str(id).zfill(cantidad_ceros) # agrego 0 a la izquierda a partir del id
    cadena_completa = digito + str(ceros) # concateno todas las cadenas
    return cadena_completa
    
#2.2
def stark_generar_codigos_heroes(lista : list):
    contador = 0
    for diccionario in lista:
        if type(diccionario) is dict and len(lista) > 0 :
            contador += 1
            id = generar_codigo_heroe (diccionario, contador)
            nombre = stark_imprimir_nombre_con_iniciales(diccionario)
            cadena_completa = f"{nombre} | {id}"
            print(cadena_completa)
        else:
            return False


#3.1
def sanitizar_entero(numero_str : str):
    numero_str.strip()
    if not numero_str.isdigit() and numero_str[0] != "-":
        return "-1" 
    try:
        numero = int(numero_str)
        if numero < 0:
            return "-2"
        return numero
    except:
        return "-3"
        

#3.2
def sanitizar_flotante(numero_str : str):
    numero_str.strip()
    if not numero_str.isdigit() and numero_str[0] != "-" and numero_str.count(".") < 1:
        return "-1" 
    try:
        numero = float(numero_str)
        if numero < 0:
            return "-2"
        return numero
    except:
        return "-3"

#3.3
def sanitizar_string(valor_str : str, valor_por_defecto : str):
    verificar = (re.search("[0-9]", valor_str))
    if verificar:
        return "N/A"
    else:
        reemplazo = valor_str.replace("/"," ")
        reemplazo = reemplazo.lower()
        valor_por_defecto = valor_por_defecto.lower()
        if reemplazo == "":
            return valor_por_defecto

    return reemplazo

#3.4
def sanitizar_dato(heroe : dict, clave : str, tipo_dato : str):
    tipo_dato = tipo_dato.lower()
    tipo_dato = tipo_dato.strip()
    if tipo_dato != "entero" and tipo_dato != "string" and tipo_dato != "flotante":
        respuesta = "Tipo de dato no reconocido"

    if clave in heroe:
        variable = heroe[clave]
        match tipo_dato:

            case "entero":
                respuesta = sanitizar_entero(variable)

            case "flotante":
                respuesta = sanitizar_flotante(variable)

            case "string":
                respuesta = sanitizar_string(variable, "-")
    return respuesta

#3.5
def stark_normalizar_datos(lista_heroes : list):
    if len(lista_heroes) == 0:
        return "Error: Lista de héroes vacía"
    else:
        for diccionario in lista_heroes:
            if len(diccionario["color_pelo"]) == "":
                diccionario["color_pelo"].replace("","No tiene")
            sanitizar_dato(diccionario, "altura", "flotante")
            sanitizar_dato(diccionario, "peso", "flotante")
            sanitizar_dato(diccionario, "fuerza", "entero")
            sanitizar_dato(diccionario, "color_ojos", "string")
            sanitizar_dato(diccionario, "color_pelo", "string")

#4.1
def stark_imprimir_indice_nombre(lista_heroes : list):
    lista_nombres = []
    for diccionario in lista_heroes:
        nombre = diccionario["nombre"]
        nombre = nombre.lower()
        nombre = re.sub("the","", nombre)
        nombre = nombre.split()
        nombres_formateados = '-'.join(nombre)
        lista_nombres.append(nombres_formateados)
    for i in lista_nombres:
        print( i, end = "-")

#5.1
def generar_separador():