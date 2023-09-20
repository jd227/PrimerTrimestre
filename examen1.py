
"""
Escriba un código en Python que mediante el uso de dos ciclos for (para imprimir la matriz), genera una matriz, con los datos ingresados por el usuario en este estricto orden: 1,2,3,4,5 y el resultado en la matriz sea, evite el uso de funciones especiales (agrega el archivo en python por favor):
1 0 0 0 0

0 2 0 0 0

0 0 3 0 0

0 0 0 4 0

0 0 0 0 5
"""
contador= 0 
for filas in range (5):
    for columnas in range (5):
        if columnas == filas:
            contador +=1 
            print( contador, end=" ")
        else: 
            print(0, end=" ")
    print()
