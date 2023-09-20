import random
n = int(random.randint(0,50))
matriz = [[0]*n for _ in range(n)]
for j in range(n):
    matriz[0][j] = 1
    matriz[n -1][j]=1
for i in range(1, n // 2 ):
    for j in range(i, n - i):
        matriz[i][j]= 1
        matriz[n- i-1][j] = 1
for filas in matriz:
    for elementos in filas:
        print(elementos, end =" ")
    print()
print(f"el tamaño de la matriz es: {n}")





