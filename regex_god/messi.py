import re

print(re.search(" ", "Lionel Messi Campeon del mundo")) # Busca el " " en la cadena de string y devuelve match y una tupla
print(re.search(" ", "Lionel Messi Campeon del mundo").span()) # Busca el " " en la cadena de string y devuelve una tupla con las posiciones de esta el ""
print(re.search(" ", "Lionel Messi Campeon del mundo").start())# Es lo mismo pero devuelve la primera posicion
print(re.search(" ", "Lionel Messi Campeon del mundo").end()) # Es lo mismo pero solo devuelve la ultima posicion
print(re.search("[0-9]+", "Lionel Messi Campeon del mundo 2022")) # Busca un solo numero (el primero) del 0 al 9 pero con el + puede devovler mas de uno "2022"
print(re.search("[0-9]+", "Lionel Messi Campeon del mundo 2022").group())# Es lo mismo pero devuelve el 2022

texto = "Jorge a Drexler sd asdsdasd 2020"
print(re.findall("[a-zA-Z]",texto))
print(re.findall("[a-zA-Z]",texto)) # devuelve todas las letras pór separado de la "a" a la "z"
print(re.findall("[a-zA-Z]{3,6}",texto)) # es lo mismo pero con un minimo de 3 letras y un maximo de 6
print(re.findall("[0-9]",texto)) # devuelve todos los numeros del 0 al 9
print(re.findall("[0-9]+",texto)) # Es lo mismo pero devuelve todos los numeros concatenados

texto2 = re.sub("[0-9]","#", texto) #reemplaza la condicion por el "#"
print(texto2)









zero = 1111110
# uno = 0110000
dos = 1101101
tres = 1111001
# cuatro = 0110011
cinco = 1011011
seis = 1011111
siete = 1110000
ocho = 1111111
nueve = 1110011

lista = list(zero)
print(lista)