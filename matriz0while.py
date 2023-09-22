# crea una matriz de tamaño aleatorio y de numeros aleatorios 

import random
def aleatorio():
    matriz=[]
    i,j,n=0,0,10
    while i<10: #Ciclos para llenarla matriz vacia
        j,aux=0,0
        while j<10: #ciclo para las columnas.
            aux=random.randint(0,9)
            matriz.append(aux)
            print(aux,end=" ")
            j+=1
        print()
        i+=1
