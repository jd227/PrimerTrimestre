n=int(input("ingresa las dimensiones n: "))
matriz=[[0]*n for _ in range(n)]
for fila in range(n):#ciclo para llenar matriz
    for columna in range(n):     
        matriz[fila][columna]= 1
for fila in range(n):# Ciclo para imprimir
    for columna in range(n):
        if (fila>=columna and columna<=5) or (fila<=columna and columna<=5):    
        #if columna==(n-fila-1):#cambio para inversa
            print(0 , end=" ")
        else:
            print(matriz[fila][columna], end= " ")
    print()