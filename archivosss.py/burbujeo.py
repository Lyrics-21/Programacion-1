arreglo = [2,1,9,10,15,123,72,57,321]

bandera = False
while bandera == False:
    bandera = True
    for i in range(len(arreglo)-1):
        if arreglo[i] > arreglo[i+1]:
            auxiliar = arreglo[i]
            arreglo[i] = arreglo[i+1]
            arreglo[i+1] = auxiliar
            bandera = False


print(arreglo)