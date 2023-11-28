from clases import Personaje
# def inicializar(diccionario, id, nombre, puede_volar, usa_nano):
#     diccionario["id"] = id
#     diccionario["nombre"] = nombre
#     diccionario["puede_volar"] = puede_volar
#     diccionario["usa_nano"] = usa_nano

# def mostrar_personaje(diccionario):
#     print(f"{diccionario['id']} - {diccionario['nombre']} - {diccionario['puede_volar']} - {diccionario['usa_nano']}")


# personaje = {}
# inicializar(personaje, 1, "IronMan", True, True)
# mostrar_personaje(personaje)

#################################################################

personaje = Personaje(5, "IronMan", True, True, 150)
print(personaje.mostrar_descripcion())

otro_personaje = Personaje(21, "Thor", True, False, 358)
print(otro_personaje.mostrar_descripcion())

personaje.fight(otro_personaje)