import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

# lista_nombres = []
# lista_monto = []
# lista_instrumento = []
# lista_tipos = []
lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]

lista_monto = [50000, 20000, 40000, 90000, 10,]

lista_instrumento = [175, 200, 150, 175, 150,]

lista_tipos = ["BONOS", "BONOS", "MEP", "BONOS", "BONOS",]
#Validacion de datos
# while True:
#     nombre = prompt("Datos","Ingrese su nombre")
#     while not nombre.isalpha():
#         nombre = prompt("Datos","Ingrese un nombre valido")

#     monto = prompt("Datos","Ingrese un monto no menor a 10000$")
#     while not monto.isdigit() or int(monto) < 10000:
#         monto = prompt("Datos","Ingrese un monto valido, no menor a 10000$")

#     instrumento = prompt("Datos","Ingrese la cantidad de instrumentos")
#     while not instrumento.isdigit():
#         instrumento = prompt ("Datos","Ingrese una cantidad valida")

#     tipo = prompt("Datos","Ingrese el tipo (BONOS,MEP,CEDEAR)")
#     while tipo != "BONOS" and tipo != "MEP" and tipo != "CEDEAR":
#         tipo = prompt("Datos","Ingrese un tipo valido (BONOS,MEP,CEDEAR)")

#     lista_nombres.append(nombre)
#     lista_monto.append(monto)
#     lista_instrumento.append(instrumento)
#     lista_tipos.append(tipo)

#     respuesta = question ("Datos","¿Desea continuar?")
#     if respuesta == False:
#         break
#Variables punto 1
bonos = 0
mep = 0
cedear = 0
tipo_mayor = 0
tipo = ""
#Variables punto 2 y 3
cantidad = 0
inversion_minima_bonos= 0
inversion_minima_mep= 0
posicion_bonos = 0
posicion_mep = 0

bandera_bono = True
bandera_mep = True

rango = len(lista_nombres)
for i in range(rango):
    nombres = lista_nombres[i]
    montos = lista_monto[i]
    instrumentos = lista_instrumento[i]
    tipos = lista_tipos[i]
    montos = int(montos)
    instrumentos = int(instrumentos)
    print (f"{nombres} - {montos}$ - {instrumentos} - {tipos}") #mostrar listas

    match(tipos):
        case "BONOS":
            bonos += 1
            if (instrumentos <= 200 and instrumentos >=150) and montos >= 50000:# punto 2
                cantidad +=1
            if (montos < inversion_minima_bonos) or bandera_bono: #punto 3
                inversion_minima_bonos = montos
                bandera_bono = False
                posicion_bonos = i
        case "MEP":
            mep += 1
            if (montos < inversion_minima_mep) or bandera_mep: #punto 2
                inversion_minima_mep = montos
                bandera_mep = False
                posicion_mep = i
        case "CEDEAR":
            cedear += 1

if bonos > mep and bonos > cedear:
    tipo_mayor = bonos
    tipo = "BONOS"
elif mep > bonos and mep > cedear:
    tipo_mayor = mep
    tipo = "MEP"
elif cedear > bonos and cedear > mep:
    tipo_mayor = cedear
    tipo = "CEDEAR"

# punto 3
nombre_minimo_bono = lista_nombres[posicion_bonos]
instrumentos_minimo_bono = lista_instrumento[posicion_bonos]

nombre_minimo_mep = lista_nombres[posicion_mep]
instrumentos_minimo_mep = lista_instrumento[posicion_mep]

print (f"Tipo de instrumentos mas operado: {tipo} ({tipo_mayor})")
print (f"Cantidad de usuarios que compraron entre 150 y 200 BONOS: {cantidad}")

print(f"{nombre_minimo_bono} compro {instrumentos_minimo_bono} BONOS e invirtio {inversion_minima_bonos}$")
print(f"{nombre_minimo_mep} compro {instrumentos_minimo_mep} MEP e invirtio {inversion_minima_mep}$")


