# PUNTO 1
from funciones import calcular_area_circulo

radio = 15
area_circulo = calcular_area_circulo(radio)

print(f"El area de un circulo con radio = {radio} es de {area_circulo} cm")

#PUNTO 2
from funciones import par_impar
numero = 23
respuesta = par_impar(numero)

#PUNTO 3
from funciones import suma_lista_numeros

lista_numeros = [1, 5, 45, 54, 123, 78, 1, 34, 89, 23, 21]
suma_lista = suma_lista_numeros(lista_numeros)
print (f"\nLa suma de todos los elementos de la lista es de {suma_lista}")

#PUNTO 4
from funciones import maximo_lista

lista_numeritosxd = [12, 324, 456, 23, 12]
mayor = maximo_lista(lista_numeritosxd)
print(f"\nEl numero mas grande de la lista es el numero {mayor}")

#PUNTO 5
from funciones import invertir_cadena

cadena_string = "Lionel Andres Messi"
cadena_invertida = invertir_cadena(cadena_string)
print(f"\n{cadena_invertida}\n")

#PUNTO 6
from funciones import ordenar_palabras

lista_palabras = ["Porfa", "Dime", "Que", "Lo", "Notas", "Losing", "Interest", "Messi", "Randalf"]
palabras_ordenadas = ordenar_palabras(lista_palabras)
for lista in palabras_ordenadas:
    print(lista)
print()

#PUNTO 7
from funciones import potencia

base = 21
exponente = 4
resultado = potencia(base,exponente)
print(f"{base} elevado a la {exponente} es {resultado}\n")

#PUNTO 8
from funciones import lista_par_impar

lista_numeros_parimpar = [12, 23, 345, 12, 56, 567, 21, 34, 1, 3, 45, 1233]
lista_par_impar(lista_numeros_parimpar)
print()

#PUNTO 9

from funciones import lista_producto

lista_numeros_producto = [23, 43, 21]
producto_de_lista = lista_producto(lista_numeros_producto)
print(producto_de_lista)
print()

#PUNTO 10
from funciones import cadena_palindromo

frase = "alagordadrogala"
cadena_palindromo(frase)









