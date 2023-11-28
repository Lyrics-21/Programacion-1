import os



#############################################################################
#ESCRITURA

# archivo = open("Nombre del archivo", modo)
# archivo = open("nombre.txt","w")
# print("C:\\Users\\marga\\OneDrive\\archivos\\nombre.txt","w")


# #Metodo write me escribir info en el archivo.
# archivo.write("Hola 1BD") #escribir en el archivo, si no existe lo crea.
# archivo.close()#Cierre el archivo, libera la info en memoria.

#############################################################################
#LECTURA

#PASO 1: Abro el archivo
# if os.path.exists("hola.txt"):
#     archivo = open("hola.txt","r")

#     #PASO 2: lo manipulo
#     informacio_archivo = archivo.read() #Si dentro del () pongo un numero, lee hasta esa cantidad de caracteres
#     print(informacio_archivo)
#     print(archivo.mode) #printea el modo, en este caso "r"
#     print(archivo.name) #printea el nombre del archivo
#     #PASO 3: Lo cierro
#     archivo.close()
#     #print(archivo.closed)
# else:
#     print("Error")

####################--READLINES--################################################
# #PASO 1: Abro el archivo
# archivo = open("hola.txt","r")
# if os.path.exists("hola.txt"):
#     #PASO 2:Lo manipulo
#     for linea in archivo.readlines():
#         #linea = linea.replace("\n","")
#         print(linea, end="") #El END evita si le paso un string vacio, no me muestra el salto en linea.
        
#         #PASO 3: Lo cierro
#     archivo.close()

##################################################################################
# #PASO 1: Abro el archivo
# archivo = open("hola.txt","r")
# if os.path.exists("hola.txt"):
#     #PASO 2:Lo manipulo
#     for linea in archivo:
#         #linea = linea.replace("\n","")
#         print(linea, end="") #El END evita si le paso un string vacio, no me muestra el salto en linea.
        
#         #PASO 3: Lo cierro
#     archivo.close()

######################--READLINE--####################################

#PASO 1: Abro el archivo
# archivo = open("hola.txt","r")
# if os.path.exists("hola.txt"):
#     #PASO 2:Lo manipulo
#     primer_linea = archivo.readline()
#     segunda_linea = archivo.readline()
#     #linea = linea.replace("\n","")
#     print(primer_linea, end="") #El END evita si le paso un string vacio, no me muestra el salto en linea.
#     print(segunda_linea)
#     print(archivo.tell()) #Indica cuantos bytes hay
#     #PASO 3: Lo cierro
#     archivo.close()

# ###########--WRITELINES--##############################################

# #Escribo una lista

# archivo = open("hola.txt","r")
# lineas_texto = ["Juan\n","Jose\n","Mauro\n"]
# archivo.writelines(lineas_texto)
# archivo.close()


# ###########--SEEK--##############################################

#PASO 1: Abro el archivo
# archivo = open("hola.txt","r")
# if os.path.exists("hola.txt"):
#     #PASO 2:Lo manipulo
#     archivo.seek(1) #Me muevo al byte que se indique en el ()
#     primer_linea = archivo.readline()
#     segunda_linea = archivo.readline()
#     #linea = linea.replace("\n","")
#     print(primer_linea, end="") #El END evita si le paso un string vacio, no me muestra el salto en linea.
#     print(segunda_linea)
#     print(archivo.tell()) #Indica cuantos bytes hay
#     #PASO 3: Lo cierro
#     archivo.close()

# if os.path.exists("hola.txt"):
#     #Abre el archivo
#     with open("archivo.txt", "r+") as archivo:
#         #PASO 2:Lo manipulo
#         for linea in archivo:
#             print(linea, end="")
#         #estoy en el with
#         print(archivo.closed)
#     #Salgo del with
#     print(archivo.closed)
# else:
#     print("Error")

############--APPEND--################################
# #Escribo una lista

with open("nombre.txt","a") as archivo:
    archivo.write("\nHola a todos")
    archivo = open("hola.txt","r")
    lineas_texto = ["Juan\n","Jose\n","Mauro\n"]
    archivo.writelines(lineas_texto)
    archivo.close()
