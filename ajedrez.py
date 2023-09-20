import random

n = int(random.randint(0,20))

if n % 4 != 0:
    print("manito manoto aqui no es mi papito")
else:
    matriz = []

    for fila in range(n):
        fila_matriz = []
        for columna in range(n):
            if (fila // 4) % 2 == 0:
                if (columna // 4) % 2 == 0:
                    fila_matriz.append(1)
                else:
                    fila_matriz.append(0)
            else:
                if (columna // 4) % 2 != 0:
                    fila_matriz.append(1)
                else:
                    fila_matriz.append(0)
        matriz.append(fila_matriz)

    # Imprimir la matriz
    
    
    for fila in matriz:
        print(' '.join(map(str, fila)))
print(f"el tamaño de la matriz es: {n}")



