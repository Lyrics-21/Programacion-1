diccionario = {"nombre" : "JORGE", "edad" : 35, "mostro" : "MESSI"}

lista_2 = ["pelado", diccionario, "messi"]

# for lista in lista_2:
#     if type(lista) == dict:
#         print(diccionario["nombre"])
        

for claves in diccionario:
    print(f"{claves} - {diccionario[claves]}\n")



def obtener_nombre(diccionario : dict, key : str):
        print(diccionario[key])

obtener_nombre(diccionario, "edad")






# lista_empleados = []
# un_empleado = {}
# nombre = input("Igrese su nombre")
# un_empleado["nombre"] = nombre

# lista_empleados.append(un_empleado)


# for a in lista_empleados:
#     print(a["nombre"])
