# PUNTO 1
import math
def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

#PUNTO 2
def par_impar(numero):
    if numero % 2 == 0:
        print("\nEl numero es par")
    else:
        print("\nEl numero es impar")

#PUNTO 3
def suma_lista_numeros(lista_numeros):
    suma_total = 0
    for suma in lista_numeros:
        suma_total += suma
    return suma_total

#PUNTO 4
def maximo_lista(lista_numeritosxd):
    maximo = 0
    for mayor in lista_numeritosxd:
        if int(mayor) > maximo:
            maximo = int(mayor)
    return maximo

#PUNTO 5
def invertir_cadena(cadena_string):
    cadena_invertida = ""
    for letra in cadena_string:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

# PUNTO 6
def ordenar_palabras(lita_palabras):
    lista_palabras_ordenadas = sorted(lita_palabras)
    return lista_palabras_ordenadas

#PUNTO 7
def potencia(base, exponente):
    resultado_potencia = base**exponente
    return resultado_potencia

#PUNTO 8
def lista_par_impar(lista_numeros_parimpar):
    for numero in lista_numeros_parimpar:
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")

#PUNTO 9
def lista_producto(lista_numeros_producto):
    multiplicacion = 1
    for multi in lista_numeros_producto:
        multiplicacion *= multi
    return multiplicacion 

#PUNTO 10
def cadena_palindromo(frase):
    inversion = ""
    for letra in frase:
        inversion = letra + inversion
    if frase == inversion:
        print(f"la frase {frase} es palindroma {inversion}")   

        


